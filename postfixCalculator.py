def get_token_list(expr):
  operator_token = [] # 연산자 list
  token_list = [] # infix 수식이 들어가는 list
  operator_lst = ['+', '-', '*', '/', '^', '(', ')'] # 연산자 list

  for op in expr: # 연산자를 연산자 list에 append
    if op in operator_lst:
      operator_token.append(op)

  for i in operator_lst: # 구분해야할 연산자를 모두 '_'로 바꿔준다
    expr = expr.replace(i, '_')
  token_list = expr.split('_') # '_'를 기준으로 split 해서 피연산자 list 생성

  for i, op in enumerate(operator_token): # 피연산자 elements 사이에 연산자를 insert해서 token_list를 만든다
    token_list.insert(2 * i + 1, op)

  token_list = [n for n in token_list if (n and not n == ' ')] # 공백 원소 제거

  return token_list ##### 피연산자에 공백이 포함되어있는 것 주의

def infix_to_postfix(token_list):
  op_stack = [] # operation stack
  out_stack = [] # postfix로 변환된 수식이 들어가는 stack
  operator_priority = {'+':1, '-':1, '*':2, '/':2, '^':3, '(':4, ')':0}

  for op in token_list:
    if op in operator_priority:
      if not len(op_stack):
        op_stack.append(op)
      else:
        if op == '(':
          op_stack.append(op)
        elif op == ')':
          while op_stack[-1] != '(':
            out_stack.append(op_stack.pop())
          op_stack.pop()
        else:
          for _ in range(len(op_stack)):
            new_op_pri = operator_priority[op]
            last_op_pri = operator_priority[op_stack[-1]]
            if new_op_pri > last_op_pri or last_op_pri == 4:
              break
            else:
              out_stack.append(op_stack.pop())
          op_stack.append(op)

        
      
    else: # op가 피연산자일 경우 out_stack에 append
      out_stack.append(op)


  
  for _ in range(len(op_stack)): # 모든 token_list 순회 후 op_stack을 비워줌
    out_stack.append(op_stack.pop())

    out_stack = [n for n in out_stack if not (n == '(' or n == ')')] # 괄호 제거

  return out_stack

def compute_postfix(token_list):
	operator_mapping = {'+':0, '-':1, '*':2, '/':3, '^':4, '(':5, ')':6}
	op_stack = []

	for op in token_list:
		if op in operator_mapping: # 연산자가 나오면 stack에서 두개값을 pop 후 연산 / 연산 후 값을 다시 stack에 append
			operator_num = operator_mapping[op]
			operation = float(op_stack.pop())
			cur_calc = float(op_stack.pop())
			if operator_num == 0:
				res = cur_calc + operation
			elif operator_num == 1:
				res = cur_calc - operation
			elif operator_num == 2:
				res = cur_calc * operation
			elif operator_num == 3:
				res = cur_calc / operation
			elif operator_num == 4:
				res = cur_calc ** operation
			op_stack.append(res)

		else : # 피연산자는 stack에 append
			op_stack.append(op)

	return op_stack[0]

	
	
	
# 아래 세 줄은 수정하지 말 것!
expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)
