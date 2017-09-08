#### Python 基本特性
##### 数据类型
* `整数`，`浮点` 与其他语言一致. `a = 1` 表示a是整数，`a = 1.23`表示a是浮点
* `字符串` 以单引号或者双引号包起来的文本。 `a = '123'`, `a = "123"` 表示a是字符串
* `布尔值` `True`或`False`.可以用 `and`, `or`, `not`表示与或非
* `\` 转义符 如 a = 'Hello \"world\"' 表示 a = `Hello "world"` `\n` 换行，`\t` 制表符，`r''` 表示''内部的的字符串不转义
##### 数据类型检查
* 数据类型检查可以使用`isinstance(object, classinfo)`，如可以使用`isinstance(x, int)`检查x是否是int，可以使用isinstance(x,(int, float))检查x是否是int或者float类型
* class 检测可以使用`issubclass(class, classinfo)`, 检测class是否是classinfo 的子类

##### 流程控制
###### if
```
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
```
```
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
```
###### for in
```
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
```
###### while 
```
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
```
##### 函数
###### 声明
声明函数需要用到关键字 `def`，然后一次写出函数名，括号，括号中的参数，和冒号`:`,如：
```
def helloPython(x):
    print('Hello python', x)
```
声明一个空方法:
```
def empty():
    pass
```
可以使用`@classmethod`表示该方法是类方法


