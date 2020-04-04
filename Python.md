#### Python开发环境搭建
1. 开发环境搭建就是安装Python的解释器
2. Python 解释器分类：
	> - CPython: C语言编写
	> - PyPy: Python语言编写
	> - IronPython: .net语言编写
	> - Jython: Java语言编写
3. 步骤：
	1. 下载安装包
		> - 3.x
		> - 2.x
	2. 安装
	3. 打开命令行窗口，输入python进行验证

#### Python 与 Sublime整合
1. 在Sublime中执行Python代码，Ctrl+B 自动在Sublime内置控制台中执行
2. 在Sublime中安装SublimeREPL插件，然后设置快捷键使用

#### 基本语法
1. 严格区分大小写
2. 每一行就是一条语句，以换行结束
3. 每一行语句不要过长，规范建议不要超过80字符
4. 一条语句可以多行编写，以反斜杠(\)结尾
5. 缩进严格，不要随便缩进
6. #为单行注释，多行注释用三个单引号 ''' 或者三个双引号 """ 将注释括起来

#### 字面量与变量
1. 字面量就是一个一个的值，表示的就是其字面值
2. 变量可以用来保存字面量，并且保存的值可以变更，根据不同的字面量表示不同的字面量

#### 变量与标识符
1. 变量
	> - 使用变量，不需要声明，直接为变量赋值即可
	> - 不能使用没有赋值的变量
	> - Python是一个动态类型的语言，可以为变量赋任意类型的值，也可以任意的改变变量的值
2. 标识符
	> - 可以包含字母、数字、下划线，但是不能以数字开头
	> - 标识符不能为关键字和保留字
	> - 不建议使用Python内置函数名作为标识符

#### 数据类型
1. 数值分三种：整数，浮点数，复数
2. 整数都是int类型
3. 整数大小没有限制，可以是一个无限大的整数
4. 如果数字长度过大，可以使用下划线作为分隔符
5. 十进制不能以0开头
6. 二进制以0b开头
7. 八进制以0o开头
8. 十六进制以0x开头
9. 浮点数运算可能得到一个不准确的结果

#### 字符串
1. 字符串需要使用引号引起来，单引号和双引号都可以，但不能混用
2. 长字符串，使用三个单引号或三个双引号，可以进行换行，并会保留格式
    ```python
    s = '''锄禾日当午，
    汗滴禾下土，
    谁知盘中餐，
    粒粒皆辛苦。'''
    ```
3. 转义字符，可以使用\作为转义字符， \uxxxx表示Unicode编码
4. 字符串格式化
	- 两个字符串可以进行相加
	- 字符串不能与其他类型进行加法运算
	- 可以使用print("a=", a)
	- 也可使用指定占位符的方式，%s表示任意字符串
	- %f 浮点数占位符
	- %d 整数占位符
        ```python
        b= 'hello %s'%'孙悟空'
        b= 'hello %s 你好 %s'%('tom', '孙悟空')
        b= 'hello%3s'%'ab' #3的含义是字符串最少三个，不足时会用空格填充，即b=hello ab
        b= 'hello%3.5s'%'abcdefg' #3.5表示字符串最少3个最多5个
        b= 'hello %f'%123.4     #表示浮点数
        b= 'hello %.2f'%123.456 #表示保留2位小数
        b= 'hello %d'%123
        ```
	- 可以通过在字符串前加一个f来创建一个格式化字符串
        ```python
        a= tom
        b= 123
        c = f'hello {a} {b}'
        ```
5. 复制字符串(将字符串和数字相乘)
    ```python
    a = 'abc'
    a = a * 2
    print(a) # 会打印abcabc
    ```

#### 布尔值与空值
1. 布尔值主要用来做逻辑判断，True表示真，False 表示假
2. 布尔值实际上属于整型，True相当于1，False相当于0
3. None 表示空值，专门用来表示不存在

#### 类型检查
1. type()用来检查值得类型
	> - print(type(1)) #<class 'int'>
	> - print(type(1.5)) #<class 'float'>
	> - print(type(True)) #<class 'bool'>
	> - print(type('hello')) #<class 'str'>
	> - print(type(None)) #<class 'NoneType'>

#### 对象(object)
1. Python是一门面向对象的语言
2. 一切皆对象
3. 程序运行当中，所有数据都是存储到内存当中然后再运行的
4. 对象就是内存中专门用来存储指定数据的一块区域
5. 对象实际上就出一个容器，专门用来存储数据
6. 数值、字符串、布尔值、None都是对象

#### 对象的结构
1. 每个对象都要保存三中数据
	1. id(标识):
		> - 用来标识对象的唯一性,
		> - 可以通过id()函数来查看对象id
		> - id由解释器生成，在CPython中，id为对应对象的内存地址
		> - 对象一旦创建，则它的id永远不再改变
	2. type(类型):
		> - 标识当前对象的所属类型
		> - int str float bool...
		> - 对象一旦创建，类型不再改变
	3. value(): 
		> - 值就是对象中存储的具体数据
		> - 对于有些对象值是可以改变的
		> - 两大类，可变对象、不可变对象

#### 变量与对象
1. 对象并没有直接存储到变量中，在Python中变量更像是给对象起了一个别名
2. 变量中存储的不是对象的值，而是对象的id(内存地址)
3. 变量中保存的对象，只有在为变量重新复制时才会改变
4. 变量与变量之间是相互独立的，修改一个变量不会影响另外一个变量

#### 类型转换
1. 所谓的类型转换，将一个类型的对象转换为其他对象
2. 类型转换不是改变对象本身的类型，而是将对象的值转换为新的对象
3. 类型转换四个函数 int() float() str() bool()

#### 运算符
1. 算术运算符
	> - \+ 加法 如果是两个字符串之间进行加法运算，则会进行拼串操作
	> - \- 减法 
	> - \* 乘法 如果将字符串与数字相乘，则会对字符串进行复制操作，重复指定次数
	> - / 除法 运算结果总会是一个浮点类型
	> - // 整除，只会保留计算后的整数位
	> - ** 幂运算
	> - % 取模
2. 赋值运算符
	> - = 将右侧值赋值给左侧的变量
3. 关系运算符
	> - 关系运算符用来比较两个值之前的关系，总会返回一个布尔值
	> - 如果关系成立，返回True, 否则返回False
	> - \> 比较左侧值是否大于右侧值
	> - \>= 比较左侧值是否大于或等于右侧值
	> - < 比较左侧值是否小于右侧值
	> - <= 比较左侧值是否小于或等于右侧值
	> - == 比较两个对象的值是否相等
	> - != 比较两个对象的是否不相等
	> - 相等与不相等比较的是对象的值，而不是id
	> - is 比较两个对象是否是一个对象，比较的是对象的id
	> - is not 比较两个对象是否不是同一个对象，比较的也是对象的id
	> - 当对字符串进行比较时，实际比较的是字符串的Unicode编码
	> - 比较两个字符串的Unicode编码时，是逐位比较的
4. 逻辑运算符
	1. not 逻辑非
		> - not 可以对符号右侧的值进行非运算
		> - 对于布尔值，非运算会对其进行取反操作
		> - 对于非布尔值，非运算会先将其转换为布尔值，然后再取反
	2. and 逻辑与
		> - 可以对符号两侧的值进行与运算
		> - 只要有个为False,则结果为False
		> - 短路与，如果第一个值为False,则不再看第二个值
	3. or 逻辑或
		> - 可以对符号两侧的值进行或运算
		> - 或运算两个值中只要有一个True,则结果为True
		> - 短路或，如果第一个值为True,则不再看第二个值
5. 非布尔值的与或运算
	1. 当我们对非布尔值进行与或运算时，Python会将其当做布尔值运算，最终会返回原值
        ```python
        result = 1 and 2 #2
        result = 1 and 0 #0
        result = 0 and 1 #0
        ```
6. 条件运算符（三目运算符）
	> - 语法:True_statements if expression else False_statements
	> - 执行流程：先对expression进行求值
	>   > 1. 如果判断结果为True，则执行True_statements，并返回结果
	>   > 2. 如果判断结果为False，则执行False_statements，并返回结果
7. 运算符的优先级
	> - 和数学中一样，在Python运算也有优先级，比如先乘除，后加减
	> - 运算符的优先级可以根据优先级表格(官方文档的Operator precedence)来查询，在表格中位置越靠下的优先级越高
 
#### input()函数
1. 该函数用来获取用户的输入
2. input() 调用后，程序会立即暂停，等待用户输入
	> - 用户输入完内容以后，点击回车程序才会继续向下执行
	> - 用户输入完成以后，其所输入的内容会以返回值的形式返回
 	> - 注意：input()的返回值是一个字符串
 	> - input()函数中可以设置一个字符串作为参数，这个参数将会作为提示文字显示

#### 条件判断
1. if语句
    ```python
    if condition_1:
        statement_block_1
    ```
2. if else语句
    ```python
    if condition_1:
        statement_block_1
    else:
        statement_block_2        
    ```
3. if elif else语句
    ```python
    if condition_1:
        statement_block_1
    elif condition_2:
        statement_block_2        
    else:
        statement_block_3        
    ```

#### 循环语句
1. while语句
    - while 循环:先对while后的条件表达式求值判断，如果结果为True,则执行循环体，再次执行此过程，直到判断结果为False
        ```python
        while condition:
            statement
        ```
    - while esle:在 while … else 在条件语句为 false 时执行 else 的语句块
        ```python
        while condition:
            statement
        else:
            additional_statement
        ```
2. for语句
    ```python
    for variable in sequence:
        statements
    else:
        statements
    ```

#### break和continue
1. break 语句可以跳出for和while的循环体。如果你从for或while循环中终止，任何对应的循环else块将不执行
2. continue 语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环

#### 列表(list)
    - 列表为Python中的一个对象
    - 列表可以保存多个有序的对象
    - 列表可以保存任意的对象
1. 列表的创建
my_list = [] # 创建空列表
my_list = ['Google', 'Runoob', 1997, 2000] # 创建非空列表
2. 通过索引获取列表中的元素
my_list[1] # Runoob
3. 获取列表的长度
len()
4. 删除列表中的元素
del my_list[1]
5. 索引可以为负数，如果为负数则从后向前获取元素，例如-1表示倒数第一个元素
6. 通过切片获取指定的元素
    1. 语法: 列表[起始:结束] # my_list[0:2]
        > 返回一个新的列表，左包含右不包含，不会对原列表产生影响
        > 如果省略结束位置，则会一直截取到最后 # my_list[1:]
        > 如果省略起始位置，则会从第一个元素开始截取 # my_list[:2]
        > 如果起始，结束全部省略，则相当于复制了一个相同的列表 # my_list[:]
    2. 语法: 列表[起始:结束:步长] # my_list[0:4:1]
        > 步长表示每次获取元素的间隔，默认值为1
        > 步长不能为0，但是可以为负数，
        > 如果是负数，则是从列表的后部向前取元素
7. 通用操作
    > \+ 可以将两个列表拼接为一个列表
    > \* 可以将列表重复指定的次数
    > in 检查指定元素是否存在于列表中 # 3 in [1, 2, 3]
    > not in 检查指定元素是否不存在于列表中
    > len(list) 列表元素个数
    > max(list) 返回列表元素最大值
    > min(list) 返回列表元素最小值
    > list(seq) 将元组转换为列表
8. 修改操作
    1. 通过切片来修改列表
        > 再给切片进行赋值时，只能使用序列
        > my_list[0:2] = ['str1', 'str2']
    2. 通过切片来删除元素
        > del my_list[0:2]
        > del my_list[::2]
9. 列表的方法
    > list.append(obj) 在列表末尾添加新的对象
    > list.count(obj) 统计某个元素在列表中出现的次数
    > list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
    > list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
    > list.insert(index, obj) 将对象插入列表
    > list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    > list.remove(obj) 移除列表中某个值的第一个匹配项
    > list.reverse() 反向列表中元素
    > list.sort( key=None, reverse=False) 对原列表进行排序
    > list.clear() 清空列表
    > list.copy() 复制列表
10. 列表的遍历
    1. while循环遍历
        ```python
        stus = ['张三', '李四'，'王五', '赵六']
        i=0
        while i < len(stus):
            print(stus[i])
            i += 1
        ```
    2. for循环遍历
        ```python
        for s in stus:
            print(s)
        ```
11. range()是一个函数，可以用来生成一个自然数的序列
    ```python
    r = range(5) # 生成一个这样的序列[0,1,2,3,4]
    ``` 
    > 该函数需要三个参数
    > - 起始位置(可以省略，默认为0)
    > - 结束位置
    > - 步长(可以省略，默认为1)

#### 元组(tuple)
1. 特点
    > 元组是一个不可变的序列
    > 它的操作方式基本和列表是一致的
2. 创建元组
    ```python
    my_tuple1 = () #空元组
    my_tuple2 = ('Google', 'Runoob', 1997, 2000) #非空元组
    my_tuple3 = "a", "b", "c", "d"   # 不需要括号也可以
    ```
3. 元组的解包：将元组的每一个元素都复制给一个变量
    ```python
    my_tuple3 = "1", "2", "3"
    a,b,c = my_tuple3
    print("a = ", a) # 1
    print("b = ", b) # 2
    print("c = ", c) # 3
    # 应用：交换a, b两个元素的值
    a, b = b, a
    # 在对一个元组进行解包时，变量的数量必须与元组中的数量一致
    # 可以在变量前加一个* , 这样变量将会获取元组中所有剩余的元素（但只能有一个）
    my_tuple4 = "1", "2", "3"，"4"
    a, b, *c = my_tuple4 # a=1 b=2 c=["3", "4"]
    a, *b, c = my_tuple4
    ```

#### 字典(dict)
1. 特点
    > - 字典属于一种新的数据结构，称为映射(mapping)
    > - 字典的作用和列表类似，都是用来存储对象的容器
    > - 列表存储数据的性能很好，但是查询数据的性能很差
    > - 字典中每个元素都有一个唯一的名字，通过这个唯一的名字可快速查找到指定元素
    > - 在查询元素时，字典的效率是非常快的
    > - 在字典中可以保存多个对象，每个对象都会有一个唯一的名字
    >   - 这个唯一的名字，称之为键(key)，可以通过key快速查找value
    >   - 这对象，我们称之为值(value)
    >   - 所以字典，我们也称之为键值对(key-value)结构
    >   - 每个字典中都可以有多个键值对，而每个键值对我们称之为一项(item)
2. 创建字典
    ```python
    dict1 = {}
    dict2 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
    dict3 = dict(name='张三', age='18')
    #包含双值子序列的序列可以转换为字典
    #双值序列：序列中只有两个值 [1,2] ('a', 3)
    #子序列，如果序列中的元素也是序列，我们称这个元素为子序列
    dict4 = dict([('name', '张三'),('age', 18)])
    ```
    > - 字典的key可以是任意的不可变对象(int, str, bool, tuple)
    > - 字典的value可以是任意对象
    > - 字典的key不能重复，否则将被覆盖
3. 访问字典里的值
    ```python
    dict3 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
    print(dict3['Alice'])
    ```
    > - 如果使用了字典中不存在的key，会报错
    > - get(key[, default]),获取key的字典值，如果字典中不存在该key，不会报错，返回None,还可以返回默认值
4. 常用操作
    > - len() 获取字典中键值对的个数
    > - in 检查字典中是否包含指定的key
    > - not in 检查字典中是否不包含指定的key
5. 修改字典
    > - d[key] = value 如果key存在则修改，不存在则添加
    > - setdefault(key[, default]), 可以向字典中添加key-value,如果存在key，则返回key的值，不会对字典进行操作，不存在则添加
    > - update([other]) 将其他字典中的key-value添加到当前字典中,如果有重复的key，后面的将替换前面的
    ```python
    d = {'a':1, 'b':2, 'c':3}
    d2 = {'d':4, 'e':5, 'f':6, 'a':7}
    d.update(d2)
    print(d) # {'a':7, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
    ```
6. 删除字典
    > - del dict['Name'] 删除键 'Name'
    > - dict.clear()     清空字典
    > - del dict         删除字典
    > - pop(key[,default]) 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值
    > - popitem() 随机返回并删除字典中的最后一对键和值
7. 字典的遍历
    1. keys() 返回所有的key
    ```python
    d = {'name':'张三', 'age':18, 'gender':'男'}
    for key in d.keys():
        print(d.get(key))
    ```
    2. values() 返回一个序列，序列中保存字典的value
    ```python
    d = {'name':'张三', 'age':18, 'gender':'男'}
    for value in d.values():
        print(value)
    ```
    3. items() 返回字典中所有的项，返回一个序列，序列中包含有双值子序列，双值分别为字典中的key和value
    ```python
    d = {'name':'张三', 'age':18, 'gender':'男'}
    for k,v in d.items():
        print(k, '=', v)
    ```

#### 集合(set)
1. 特点
    > - 集合和列表非常相似
    > - 集合中只能存储不可变对象
    > - 集合中存储的对象时无序的
    > - 集合中不能存在重复的元素
2. 创建集合
    ```python
    s = {1, 8, 2, 5}
    s = set() #空集合
    s = set([1,2,3])
    s = set('hello')
    s = set({'a':1, 'b':2}) #使用set()将字典转换为集合，只会包含字典的键
    ```
3. 使用in和not in来检查集合中的元素
4. 使用len(),来获取集合中的数量
5. 使用add(),向集合中添加元素
6. 集合的运算
    > & 交运算
    > | 并集运算
    > \- 差集运算
    > ^ 亦或集，只在一个集合中出现的元素
    > <= 检查一个集合是否为另外一个集合的子集
    > \>= 检查一个集合是否为另外一个的超集
    > \> 检查一个集合是否为另外一个的真超集

#### 函数
1. 函数简介
    - 函数也是一个对象
    - 对象时内存中专门用来存储数据的一块区域
    - 函数可以用来保存一些可执行的代码，并且可以在需要的时候，对这些语句进行多次调用
2. 定义函数
    ```python
    def 函数名(参数列表):
        函数体
    ```
3. 函数的参数
    - 定义函数时，可以在参数列表中定义数量不等的形参，多个形参之间用逗号隔开
    - 如果函数定义了形参，那调用函数时也必须传相应的实参
    - 参数可以指定默认值，如果用户传递了参数则默认值不生效，如果没有传递则默认值生效
        ```python
        def fn(a, b, c=20):
            print('a=', a)
            print('b=', b)
            print('c=', c)
        fn(1, 2)
        fn(1, 2, 3)
        ```
    - 位置参数就是将对应位置的实参赋值给对应位置的形参
    - 关键字参数可以不按照形参的定义顺序去传递，而直接根据参数名去传递参数
        ```python
        def fn(a, b, c=20):
            print('a=', a)
            print('b=', b)
            print('c=', c)
        fn(b=1, c=2, a=3)
        fn(1,c=30) # 混合使用关键字位置参数时，必须将位置参数写在前面
        ```
    - 函数在调用时，解析器不会检查实参的类型
    - 不定长参数，在形参前加一个\*, 这样这个形参将会获取到所有的实参，保存在一个元组中
        ```python
        def fn(*nums):
            result = 0
            for n in nums:
                result += n
            print(n)
        ```
    - 带星号的形参只能有一个
    - 带星号的参数可以与其他参数配合使用
    - 可变参数不是必须卸载最后，但带星号的参数后的所有参数，必须以关键字参数的形式传递
        ```python
        def fn(a,*nums, c):
            result = a+c
            for n in nums:
                result += n
            print(n)
        fn(1,2,3,4,c=5)
        ```
    - 如果再形参的开头直接写了一个星号，则要求我们的所有参数必须以关键字形参的传递方式
        ```python
        def fn(*， a, b , c):
            print('a=',a)
            print('b=',b)
            print('c=',c)
        fn(a=1,b=2,c=5)
        ```
    - 星号形参只能接受位置参数，而不能接收关键字参数
    - 两个星号形参可以接收其他的关键字参数，它会将这些参数统一保存在一个字典中
        ```python
        def fn(**a):
            print('a=',a) # a = {'a':1,'b':2,'c':5}
        fn(a=1,b=2,c=5)
        ```
    - 两个星号的形参只能有一个，并且必须写在所有参数的最后
    - 参数的解包，传递实参时，也可以在序列类型的参数前添加星号，这样它会自动将序列中的元素依次作为参数传递
        ```python
        t = (10, 20, 30)
        d = {'a':100, 'b':200, 'c':300}
        def fn(a, b , c):
            print('a=',a)
            print('b=',b)
            print('c=',c)
        fn(*t) # 解包元组 注意 元组的个数要与参数的个数一致
        fn(**d) # 解包字典
        ```
4. 函数返回值
    - 可以通过return来指定函数的返回值
    - return后可以跟任意的对象，甚至可以是一个函数
    - 如果只写一个return或不写return，则返回一个None
5. 文档字符串
    - help()是Python中的一个内置函数
    - 通过help()函数可以查询Python中的函数的用法
    - 在定义函数时，可以在函数内部编写文档字符串，来给函数添加说明
    - 然后可以通过help()来查看说明
        ```python
        def fn(a,b,c):
            '''
            这是一个文档字符串实例
            函数的作用：求和
            函数的参数
                a:第一个参数
                b:第二个参数
                c:第三个参数
            '''
            return a+b+c
        help(fn)
        # 注意以下函数写法，仅仅是为了调用者理解形参及返回值得类型
        # 函数本身并不会对其进行校验显示
        def fn2(a:int, b:bool) -> str:
            return "abc"
        ```

#### 作用域与命名空间
1. 作用域，是指变量生效的区域
    - 全局作用域：程序执行是创建，程序执行结束是销毁
        > 所有函数以外的区域都属于全局作用域
        > 在全局作用域中定义的变量，可以在程序任意位置被访问
    - 函数作用域：函数调用时创建，调用结束时销毁
        > 函数没调用一次就会产生一个新的函数作用域
        > 函数作用域定义的变量，只能在函数内部使用
    - 变量的查找
        > 当使用变量时，会优先在当前作用域中寻找该变量，如果有则使用
        > 如果没有则继续去上一级作用域中寻找，如果有则使用，
        > 如果依然没有则继续去上一级作用域中查找，以此类推
        > 直到找到全局作用域，依然没找到，则会抛出异常
    - 使用global关键字，可以在任意作用域定义全局变量
2. 命名空间：变量存储的位置，每个变量都需要存储到指定的命名空间当中
    - 命名空间实际上就是一个字典，是专门用来存储变量的字典
    - locals()用来获取当前作用域的命名空间
    - 如果再全局作用域调用locals()则获取全局命名空间，如果在函数作用域中调用locals()则获取函数命名空间，返回一个字典
    - globals()函数可以在任意位置获取全局的命名空间

#### 高阶函数
1. 特点
    > 接收一个或多个函数作为参数
    > 将函数作为返回值返回
2. 举例
    ```python
    # 检查一个任意的数字是否为偶数
    def fn1(i):
        if i % 2 = 0:
            return True
        return False

    # 检查指定数字是否大于5
    def fn2(i):
        if i > 5:
            return True
        return False

    #定义一个高阶函数
    def fn(func, lst):
        new_list = []
        for n in lst:
            if func(n):
                new_list.append(n)

        return new_list

    # 调用
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(fn(fn1, l))
    ```

#### 匿名函数 lambda 函数表达式
1. lambda函数表达式专门用来创建一些简单的函数，他是函数创建的又一种方式
2. 语法： lambda 参数列表: 返回值
```python
def fn(a, b):
    return a+b
# 等价于
lambda a,b : a+b
```

#### 闭包
1. 将函数作为返回值返回，也是一种高阶函数
2. 这种高阶函数我们也称之叫做闭包，通过闭包可以创建一些只有当前函数能访问的变量
3. 可以将一些私有的数据藏到闭包中
```python
def fn():
    a=10
    def inner():
        print('我是内部函数', a)

    return inner


# r 是一个函数，是调用fn()后返回的函数
# 这个函数是在fn()内部定义的，并不是全局函数
# 但是该函数总能访问到fn()函数内的变量
r = fn()
```

#### 装饰器，扩展已有函数
```python
# 原有函数
def fn(a, b):
    return a+b

def begin_end(old_function):
    #创建一个新函数
    def new_function(*args, **kwargs):
        print('开始执行。。。')
        # 调被扩展函数
        result = old_function(*args, **kwargs)
        print('执行结束。。。')
        # 返回函数执行结果
        return result
    # 返回新函数
    return new_function

f = begin_end(fn)
f(1,2)
# 向begin_end()这种函数我盟称之为装饰器，
# 通过装饰器，可以在不修改原来函数的情况下来对函数进行扩展
# 在开发中，我盟都是通过装饰器来扩展函数的功能的
# 在定义函数时，可以通过@装饰器，来使用指定的装饰器，修饰当前的函数
# 可以同时为一个函数指定多个装饰器，这样函数将会安装从内向外的顺序被装饰

@begin_end
def say_hello():
    print('大家好')

say_hello()
```
#### 类(class)
    - 我们目前所学习的对象都是Python内置对象
    - 但是内置对象不能满足所有的需求，因此在开发中需要自定义一些对象
    - 对象是类的实例
    - 如果多个类通过一个类创建，我们称这些对象是一类对象
    - 自定义的类都需要使用大写字母开头，使用大驼峰命名法(帕斯卡命名法)来对类命名
1. 定义一个简单的类
    ```python
    class MyClass:
        pass
    ````
    > isinstance()用来检查一个对象是否是一个类的实例
    > 通过MyClass()这个类创建的对象是一个空对象
    > 也就是对象中实际上什么都没有，就相当于一个空的盒子
    > 可以向对象中添加变量，对象中的变量称为属性
    > 语法： 对象.属性名 = 属性值
    ```python
    class Person:
        name = 'tom'
    ````
    > 在类的代码块中，可以定义变量和函数
    > 在类中所定义的变量，将会称为所有的实例的公共变量
    > 所有实例都可以访问这些变量
    > 类中定义的函数，称之为方法
    > 这些方法可以通过类的所有实例进行访问
    > 方法调用时，第一个参数由解析器自动传递，所有定义方法时，至少要定义一个形参
    > 第一个参数对象就是调用方法的对象本身，一般命名为self
    > 类中定义的属性和方法都是公共的，任何该类实例都可以访问
    > 在方法中不能直接访问类中的属性
2. 类的初始化
    > 在类中可以使用一些特殊的方法(魔术方法)
    > 特殊方法以\_\_(双下划线)开头，\_\_(双下划线)结尾的方法
    > 特殊方法不需要主动调用
    ```python
    class Person():
        # 对象创建时自动调用
        # 可以用于对象的初始化
        def __init__(self):
            print('__init__ excute')

        def say_hello():
            print('hello')
    ```
    > init会在对象创建以后立即执行
    > init可以用来向新创建的对象中初始化属性
    > 调用类创建对象是，类后边的所有参数都会依次传递到init()中
    ```python
    class Person():
        def __init__(self，name):
            self.name = name

        def say_hello():
            print('hello ', self.name)

    p = Person()
    p.say_hello()
    ```

#### 封装
1. 提供修改属性的方法getter和setter
    ```python
    class Dog():
        def __init__(self，name):
            self.name = name

        # getter
        def get_name(self):
            return self.name

        # setter
        def set_name(self, name):
            self.name = name
    ```
    > getter 获取对象中指定属性(get_属性名)
    > setter 设置对象的指定属性(set_属性名)
2. 属性隐藏
    > 可以为对象的属性使用双下划线开头， \_\_xxx
    > 双下划线开头的属性，是对象的隐藏属性，隐藏属性只能在类内访问，无法通过对象访问
    > 其实隐藏的属性只是Python自动为属性改了名字，改为了:\_类名__属性名
    > 使用了双下划线的属性，实际上依然可以在外部访问到
    > 一般我们会将私有属性以单下划线开头
    ```python
    class Dog():
        def __init__(self，name):
            self.__name = name

        # getter
        def get_name(self):
            return self.__name

        # setter
        def set_name(self, name):
            self.__name = name

    p = Dog('大黄')
    print(p.__name) #访问不到，会报错
    p.__name = '小黑' #修改不了，但不会报错
    ```
3. property装饰器
    ```python
    class Dog():
        def __init__(self，name):
            self._name = name

        # property装饰器用来将一个get方法，转换为对象的属性
        # 添加property装饰器以后，我们可以像调用属性一样使用get方法
        # 使用property装饰的方法，必须和属性名是一样的
        @property
        def name(self):
            return self._name

        # setter方法的装饰器： @属性名.setter
        @name.setter
        def name(self，name):
            self._name = name
    p = Dog('大黄')
    prin(p.name)
    p.name = '小黑'
    ```

#### 继承
1. 继承介绍
    - 继承是面向对象三大特征之一
    - 通过继承可以使一个类获取其他类中的属性和方法
    - 在定义类时，可以在类后面的括号中指定当前类的父类，
    - 子类可以继承父类中所有的属性和方法
    ```python
    class Animal():
        
        def run(self):
            print('动物会跑。。。')

        def sleep(self):
            print('动物睡觉。。。')

    class Dog(Animal):
        
        def bark(self):
            print('汪汪汪。。。')

    d = Dog()
    # 用来检查一个对象是否是一个类的实例
    r = isinstance(d, Animal) # True
    # 检查一个类是否为另外一个类的子类
    s = issubclass(Animal, Dog) #True

    ```
    - 通过继承可以直接让子类获取到父类的方法和属性，避免编写重复代码
    - 创建类时省略了父类，则默认继承的是object，object是所有类的父类
2. 方法重写
    - 如果子类和父类存在同名的方法，则通过子类调用实例方法时，调用的是子类的方法，而不是父类中的方法
    ```python
    class Animal():
        
        def run(self):
            print('动物会跑。。。')

        def sleep(self):
            print('动物睡觉。。。')

    class Dog(Animal):
        
        def bark(self):
            print('汪汪汪。。。')

        def run(self):
            print('狗跑。。。')

    d = Dog()
    d.run() # 会打印 狗跑。。。

    ```
    - 父类中的所有方法都会被子类继承，包括特殊方法
    - super()可以用来获取当前类的父亲
    - 并且通过super()返回对象调用父类方法时，不需要传递self
3. 多重继承
    - Python支持多重继承，一个类可以同时指定多个父类
    - 多重继承会使子类拥有多个父类，并且会获取所有父类中的方法，但开发时尽量避免使用
    - 如果多个父类中有同名的方法，则会先在第一个父类中查找，然后查找第一个父类，依次类推，前边父类的方法会覆盖后边父类的方法
    ```python
    class A(object):
        def test(self):
            print('AAA')

    class B(object):
        def test2(self):
            print('BBB')

    class C(A,B):
        def test3(self):
            print('CCC')
    ```
    - 类名.__bases__ 这个属性可以用来获取当前类的所有父亲

#### 多态
```python
class A(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

class B(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

a = A('张三')
b = B('李四')

# 对于say_hello()函数来说，只要对象含有name属性，它就可以作为参数传递
# 这个函数不会考虑对象的类型，只要有name属性即可
def say_hello(obj):
    print('你好：', obj.name)
say_hello(a)
say_hello(b)

# 在say_hello2()中，我们做了类型检查，也就是只有obj类型是A类型的对象时，才可以正常使用
# 其他类型的对象都无法使用该函数，这个函数违反了多态
# 违反了多态的函数，只适用于一种类型的对象，无法处理其他类型的对象，适应性差
def say_hello2(obj):
    if isinstance(obj, A):
        print('你好：', obj.name)
say_hello2(a)
say_hello2(b)
```
    - len(),之所以一个对象能通过len()来获取长度，是因为对象中具有一个特殊方法__len__
    - 换句话说，只要对象中有__len__特殊方法，就可以通过len()来获取它的长度

#### 类的属性和方法
```python
class A():

    # 类属性，直接在类中定义的属性是类属性
    # 类属性可以通过类或类的实例访问
    # 但是类书拽只能通过类对象来修改，无法通过实例对象修改
    count = 0

    def __init__(self):
        # 实例属性，通过实例对象添加的属性属于实例属性
        # 实例属性只能通过实例对象来访问和修改，类对象无法访问修改
        self.name = '张三'

    # 实例方法
    # 在类中定义，以self为第一个参数的方法都是实例参数
    # 实例方法在调用时，Python会将调用对象作为self传入
    # 实例方法可以通过实例和类去调用
    #    当通过实例调用时，会自动将当前调用对象作为self传入
    #    当通过类调用时，不会自动传递self，此时必须手动传递self
    def test(self):
        print('test', self)

    # 类方法
    # 在类内部使用 @classmethod 来修饰的方法属于类方法
    # 类方法的第一个参数cls，也会被自动传递，cls就是当前的类对象
    # 类方法和实例方法的区别：实例方法第一个参数是self，而类的第一个参数是cls
    # 类方法可以通过类去调用，也可以通过实例调用，没有区别
    @classmethod
    def test2(cls):
        print('类方法', cls)

    # 静态方法
    # 在类中使用 @staticmethod 来修饰的方法属于静态方法
    # 静态方法不需要知道任何默认参数，静态方法可以通过类和实例去调用
    # 静态方法，基本上是一个和当前类无法的方法，它只是一个保存在当前类中的函数
    # 静态方法一般都是一些工具类方法，和当前类无关
    @staticmethod
    def test3():
        print('静态方法')

    a = A()
    a.count = 10
    A.count = 100
    print('A, ', A.count)
    print('a, ', a.count)
    print('A, ', A.name)
    print('a, ', a.name)
    # a.test() 等价于  A.test(a)
    A.test2()
```

#### 垃圾回收
- 在Python中有自动的垃圾回收机制，它会自动将这些没有被引用的对象删除
- 不需要手动处理垃圾对象
- 将一个对象设置为None，此时没有任何对象对其引用时，它就是垃圾
- __del__ 是一个特殊方法，它会在对象被垃圾回收前调用

#### 特殊方法
- 也称为魔术方法
- 特殊方法都是以__开头和结尾
- 特殊方法一般不需要手动调用，需要在一些特殊情况下自动执行

#### 模块(module)
1. 模块化
    - 将一个完整的程序分解为一个一个小的模块，通过将模块组合，来单门出一个完整的程序
    - 不采用模块化，统一将所有的代码编写到一个文件中
    - 采用模块化，将程序分表编写到多个文件中
    - 模块化优点
        1. 方便开发
        2. 方便维护
        3. 模块可以复用
    - 在Python中一个py文件就是一个模块，创建模块其实是创建py文件
    - 模块名要符合标识符规范
    - 在一个模块中引入外部模块
        1. import 模块名 (模块名，就是Python的文件名，不要后缀py)
        2. import 模块名 as 模块别名
        3. 即使引入多次同一模块，但是模块的实例创建一个
        4. import可以在程序的任意位置，但一般写在开头位置
        5. 每个模块内部都有一个__name__属性，通过这个属性可以获取到模块的名字
        6. \__name__属性值为 \__main__的模块是主模块，一个程序中只会有一个主模块
        7. 在模块中定义变量、函数、类等，可以在引入模块后进行直接使用
        8. 访问： 模块名.变量名
        9. 只引入模块中的部分内容： 
            - from 模块名 import 变量,变量...
            - from 模块名 import \*
            - from 模块名 import 变量 as 别名
        10. 在通过import * 引入模块时，被引入模块添加了_的变量，只能在模块内部访问，不会被引入到新模块
        11. 如果部分代码，只有当做主模块运行是才需要执行，而当模块呗其他模块引入时，不需要执行(例如测试代码)，此时就必须检查当前模块是否是主模块
        ```python
        if __name__ == '__main__':
            pass
        ```

#### 包 Package
1. 包也属于一种模块
2. 当模块中代码过多是，或者一个模块需要被分解为多个模块时，就需要使用包
3. 普通模块就是一个py文件，而包是一个文件夹
4. 包中必须要有一个__init__.py文件，这个文件可以包含有包中的主要内容
    - from hellp(包名) import a(模块名), b(模块名)
    - __pycache__ 是模块缓存文件，在使用模块(包)时，需要将模块代码先转换为机器码然后再交计算机执行
    - 为了提高程序运行的性能，Python会在编译过一次以后，将代码保存到缓存文件中

#### Python标准库
[官方库介绍文档地址](https://docs.python.org/3/py-modindex.html)
1. sys 模块，它里面提供了一些变量和函数，使我们可以获取到Python解析器的信息
    > sys.argv: 获取执行代码时，命令行中所包含的参数(列表类型)，其中第一个为文件名本身
    > sys.modules: 获取当前程序引入的所有模块(字典类型)
    > sys.path: 返回模块的搜索路径(列表类型)
    > sys.platform: Python运行平台(linux win32 cygwin darwin)
    > sys.exit(): 程序退出
2. pprint 模块， 它提供了一个pprint()，该方法可以用来对打印的数据进行简单的格式化
3. os 模块，可以对操作系统进行访问操作
    > os.environ: 系统环境变量
    > os.system(): 执行操作系统命令

#### 异常
1. 程序在运行过程中，不可避免的会出现一些错误，称之为异常
2. try 语句
```python
try:
    # 执行代码
    pass
except Exception as e:
    # 发生异常时执行的代码
    # 如果指定了具体的异常类型，则只会捕获该类型的异常
    # 捕获多个异常，可以写多个except
    # Exception为所有异常的父类
    raise
else:
    # 没有异常时执行的代码(可有可无)
    pass
finally:
    # 不管有没异常都会执行的代码
    # except 和 finally至少要有一个
    pass
```
3. 当函数中出现异常时
    - 如果在函数中对异常进行了处理，则异常会再继续传播
    - 如果函数中没有对异常进行处理，则异常会继续向调用函数调用处传播
    - 直到传递到全局作用域(主模块)，如果依然没有处理，则程序终止，并显示异常信息
4. 当程序运行过程中出现异常以后，所有的异常信息会被保存一个专门的异常对象中，而异常传播时，实际上就是异常对象抛给了调用处，比如 ZeroDivisionError 类
5. Python 中提供了很多异常类
    [内部异常官方文档](https://docs.python.org/3/library/exceptions.html)
6. 可以使用 raise 语句抛出异常
    > 语法： raise [Exception [, args [, traceback]]]
    > raise 唯一的一个参数指定了要被抛出的异常。
    > 它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）
7. 可以自定义异常类，只需要创建一个类继承Exception即可
    ```python
    class myError(Exception):
        pass
    ```

#### 文件(File)
1. 使用open()函数来打开一个文件
2. [官方open()介绍](https://docs.python.org/3/library/functions.html#open)
3. open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    > file: 必需，文件路径（相对或者绝对路径）
    > mode: 可选，文件打开模式
    > buffering: 设置缓冲
    > encoding: 一般使用utf8
    > errors: 报错级别
    > newline: 区分换行符
    > closefd: 传入的file参数类型
    > opener:
4. 代码示例
    ```python
    # 目标文件与当前文件在同一级目录，直接使用文件名即可
    file_name = 'demo.txt'
    # 可以使用\\来表示\
    file_name = 'home\\demo.txt'
    # 在windows系统可以使用/来代替\
    file_name = 'home/demo.txt'
    # 可以使用原始字符串
    file_name = r'home\demo.txt'
    # 可以使用..来返回一级目录
    file_name = '../home/demo.txt'
    # 还可以使用绝对路径
    file_name = 'D:/home/demo.txt'

    file_obj = open(file_name)
    ```
5. 关闭文件
    - file.close() 关闭文件。关闭后文件不能再进行读写操作
    - with ... as 语句
        ```python
        file_name = 'demo.txt'
        with open(file_name) as file_obj:
            # with语句中可以直接使用file_obj来操作文件
            # 此时这个文件只能在with中使用，一旦with结束则文件会自动close()
            print(file_obj.read())
        ```
6. 文件的读取
    - 例子1
        ```python
        file_name = 'demo.txt'
        try:
            # 一种纯文本文件(使用utf-8等编码编写的文本文件)
            # 一种二进制文件(图片，MP3，PPT等)
            # open()打开文件时，默认以文本文件的形式打开，但是open()默认的编码为None
            # 所以处理文本文件时，必须指定文件的编码
            with open(file_name, encoding='utf-8') as file_obj:
                # 通过read()来读取文件中的内容
                # 如果直接调用read()，它会将文本文件的所有内容全部都读取出来
                # 如果文件较大，容易导致内存溢出，所以对于较大文件不建议直接调用read()
                # read()可以接受一个size作为参数，该参数用来指定要读取的字符数量
                #   默认-1，表示要读取文件所有字符
                #   file_obj.read(6)
                #   可以为size指定一个值，这样read()会读取指定数量的字符
                #   每一次读取都是从上一次读取的位置开始读取
                #   如果字符的数量小于size()，则会读取剩余所有的
                #   如果已经读取到了文件的最后了，则会返回一个''空串
                print(file_obj.read())
        except FileNotFoundError as e:
            print(file_name, '文件不存在！')
        ```
    - 例子2， 读取大文件
        ```python
        file_name = 'demo.txt'
        try:
            with open(file_name, encoding='utf-8') as file_obj:
                # 定义一个变量来保存文件内容
                file_content = ''
                # 定义每次读取的字符数
                chunk = 100
                # 创建循环来读取文件内容
                while True:
                    # 读取chunk大小的内容
                    content = file_obj.read(chunk)
                    # 检查是否读取到了内容
                    if not content:
                        # 内容读取完毕，退出循环
                        break
                    # 输出内容
                    file_content += content
        except FileNotFoundError as e:
            print(file_name, '文件不存在！')

        print(file_content)
        ```
    - 例子3 readline()  readlines()
        ```python
        file_name = 'demo.txt'
        try:
            with open(file_name, encoding='utf-8') as file_obj:
                # readline() 该方法可以用来读取一行内容
                file_obj.readline()

                # file_obj.readlines() 一行一行读取，将结果封装成列表返回

                # 此种方法也可以一行一行读取
                # for t in file_obj
                #    print(t)
        except FileNotFoundError as e:
            print(file_name, '文件不存在！')
        ```
7. 文件的写入
    ```python
    file_name = 'demo.txt'
    try:
        # 使用open()打开文件是，必须要指定打开文件所要做的操作(读，写，追加)
        # 如果不指定操作类型，则默认是读取文件，而读取文件时是不能向文件中写入的
        # r 表示只读
        # w 表示可写，写入时如果文件不存在会创建文件，如果已经存在则会截断文件，即删除原有文件内容
        # a 表示追加, 如果文件不存在会创建文件，如果存在则追加
        # x 新建文件，如果文件不存在会创建，存在会报错
        # + 为操作符增加功能
        # r+ 可读可写，文件不存在会报错
        # w+
        # a+
        with open(file_name, mode='w' encoding='utf-8') as file_obj:
            # write()来向文件中写入内容
            # 如果操作的是一个文本文件，则write()需要传递一个字符串作为参数
            # 该方法可以多次向文件中写入， 
            # 写入完成，该方法会返回写入字符的个数
            r = file_obj.write('Hello Python!')
    except FileNotFoundError as e:
        print(file_name, '文件不存在！')
    ```
8. 二进制文件
    ```python
    file_name = 'demo.mp3'
    try:
        # 读取模式
        # t 读取文本文件(默认值)
        # b 读取二进制文件
        with open(file_name, mode='rb') as file_obj:
            # 读取文本文件时，size是以字符为单位
            # 读取二进制文件时，size是以字节为单位
            # print(file_obj.read(100))

            # 将读到的内容写入文件
            # 定义一个新的文件
            new_file_name = 'demo2.mp3'
            with open(new_file_name, 'wb') as new_obj:

                # 定义读取的大小
                chunk = 1024 * 100

                while True:
                    # 读取到的内容
                    content = file_obj.read(chunk)

                    # 判断读取完成
                    if not content:
                        break
                    # 写入新的文件
                    new_obj.write(content)

    except FileNotFoundError as e:
        print(file_name, '文件不存在！')    
    ```
9. seek() 和 tell()
    ```python
    file_name = 'demo.txt'
    try:
        with open(file_name, mode='rb') as file_obj:
            print(file_obj.read(100))

            # seek()可以修改当前读取的位置
            # seek()需要两个参数
            #  第一个 是要切换到的位置
            #  第二个 计算位置的方式
            #       可选值：
            #           0 从头计算, 默认值   file_obj.seek(130, 0)
            #           1 从当前位置计算     file_obj.seek(70, 1)
            #           2 从最后位置开始计算 file_obj.seek(-20, 2)
            # 注意，文本和二进制读取是的单位问题，一个是字符，一个是字节
            file_obj.seek(130)

            # tell() 方法用来查看当前读取的位置
            print('当前读取到了 --> ', file_obj.tell())

    except FileNotFoundError as e:
        print(file_name, '文件不存在！')    
    ```
10. 文件的其他操作
    ```python
    import os
    from pprint import pprint

    # os.listdir()获取指定目录的目录结构
    # 需要一个路径作为参数，会获取到该路径下的目录结构，默认值为. 当前目录
    # 该方法会返回一个列表，目录中的每一个文件(夹)的名字都是列表中的一个元素
    r = os.listdir()

    # 获取当前所在目录
    r = os.getcwd()

    # 切换当前所在的目录,相当于cd 命令
    r = os.chdir('..')

    # 创建目录
    os.mkdir('aaa')

    # 删除目录
    os.rmdir('aaa')

    # 删除文件
    os.remove('aa.txt')

    # os.rename('旧名字', '新名字')
    os.rename('aa.txt', 'bb.txt')
    # 实现了移动文件的功能
    os.rename('aa.txt', 'D:/home/bb.txt')

    pprint(r)

    ```