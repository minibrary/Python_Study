input_id = input("아이디를 입력해주세요.\n")
input_pwd = input("비밀번호를 입력해주세요.\n")
real_id = "josh"
real_pwd = "11"
if real_id == input_id:
    if real_pwd == input_pwd:
        print("Welcome,"+real_id)
    else:
        print("잘못된 비밀번호입니다.")
else:
    print("잘못된 아이디 입니다.")
