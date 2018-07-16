#ex10: What Was That?

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#\r: 回车: 回到当前行的行首，而不会换到下一行，如果接着输出的话，本行以前的内容会被逐一覆盖；
#\n: 换行: 换到当前位置的下一行，而不会回到行首；
s1 = "已经习惯了回车和换行一次搞定\n，敲一个回车键，即是回";
print(s1)
s1 = "123456789\r，abcd";
print(s1)
s1 = "已经习惯了回车和换行一次搞定\r\n，敲一个回车键，即是回";
print(s1)

