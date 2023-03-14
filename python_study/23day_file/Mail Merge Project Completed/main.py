PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    # line 형태롤 파일을 읽고 리스트 형태로 반환
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        # 1번째 인자에 명시된 구문을 2번째 문자열로 바꿔주는 기능을 한다.
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
