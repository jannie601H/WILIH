#include <Servo.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <TimerOne.h>

Servo myServo;
LiquidCrystal_I2C lcd(0x27, 16, 2); // adress: 0x27, cols = 16, rows = 2

//int sensorValue = 0; // 조도센서 값
int MAsetbutton = 2; // auto manual setting button pin digital input 2
int MAstate = LOW; // low for manual, high for auto
int angleSetButton = 3; // angle setting button in manual digital input 3
int manualLoop = 0; // manual angle setting loop (0 to close, 1 to half, 2 to open)
int state = 0;

void setup() {
  Serial.begin(9600); //serial monitor setting
  myServo.attach(9); // servo moter setting

  lcd.init(); // lcd setting
  lcd.backlight();

  pinMode(MAsetbutton, INPUT);
  attachInterrupt(digitalPinToInterrupt(2), MAbuttonRead, RISING); // toggle to swich manual/auto

  pinMode(angleSetButton, INPUT);
  attachInterrupt(digitalPinToInterrupt(3), angleSetButtonRead, RISING);
}

void loop() {
  int sensorValue = analogRead(A0);

  if (MAstate == HIGH) {
    // auto
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("AUTO");
    sensorValue = analogRead(A0);
  } else if (MAstate == LOW) {
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("MANUAL");
    sensorValue = manualLoop;
  }
  if (sensorValue > 500) {
    state = 2;
  }
  else if (sensorValue > 200) {
    state = 1;
  }
  else {
    state = 0;
  }
  if (state == 2) { // 500nit 이상 (직사광선)일시 블라인드 정방향 반닫힘
    lcd.setCursor(0,1);
    lcd.print("HALF"); // 블라인드 상태 lcd 출력
    // 블라인드 각 제어
    if (myServo.read() < 50) {
      for (int angle = myServo.read(); angle < 50; angle++) {
        myServo.write(angle);
        delay(30);
      }
    } 
    else {
      for (int angle = myServo.read(); angle > 50; angle--) {
        myServo.write(angle);
        delay(30);
      }
    }
  } 
  else if (state == 1) { // 200nit ~ 500nit (평상시) 블라인드 역방향 열림
    lcd.setCursor(0,1);
    lcd.print("OPEN"); // 블라인드 상태 lcd 출력
    // 블라인드 각 제어
    for (int angle = myServo.read(); angle > 10; angle--) {
      myServo.write(angle);
      delay(30);
    }
  } 
  else if (state == 0) { // 200nit 이하 (어두움) 블라인드 완전 닫힘
    lcd.setCursor(0,1);
    lcd.print("CLOSE"); // 블라인드 상태 lcd 출력
    // 블라인드 각 제어
    for (int angle = myServo.read(); angle < 105; angle++) {
      myServo.write(angle);
      delay(30);
    }
  }
Serial.println(sensorValue);  
  // Timer1.initialize(1000000); // 내부 인터럽트; 1초마다 조도센서 값 받아옴
  // Timer1.attachInterrupt(serialPrint);
}

// void serialPrint() {
//   Serial.println(sensorValue);
// }

// manual auto state interrupt switch
void MAbuttonRead() {
  MAstate = !MAstate;
}

void angleSetButtonRead() {
  if (manualLoop >= 600) {
    manualLoop = 0;
  } else {
    manualLoop += 300;
  }
}