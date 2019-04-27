import re
import dbapi

### 读取文件
#file1 = open("innerinterfaces.txt","r")
file1 = open("inin.txt","r")
str1 = file1.read()

### 数据处理
# 正则就是字符串处理,"\n"被当成了字符(ASCII值为"5C 6E"),“\n2.”就无法识别为“以2.开头”，所以去掉“r'(^[0-9]+\.)'”中的“^”.
# 正则是否带r，也有区别。有r会保留匹配的项，没有r去掉匹配的项。所以去掉“r'([0-9]+\.)'”中的“r”
# 获取ID
apikeys = re.findall(r'(^[0-9]+)\.', str1, re.M)

#获取json内容
apivalues = re.split('[0-9]+\.', str1)
# 去掉list中的第一个空对象
apivalues.pop(0)
# utf8格式中，汉字为3个ASCII字符。去掉所有的空格(ASCII值为20)和tab键(ASCII值为09)，tab一般会变成多个空格。
# 将中文的：替换为英文的:,将空格去掉，将行首的回车“^\n”替换为“”。
# 各种去掉\n。

# map转换为list
def map2list(mp):
	lst=[]
	for ll in mp:
		lst.append(ll)
	return lst

list1=apivalues;

trans1=[('：',':'),(' ',''),('^\n',''),('(\n)+','\n'),('\n}','}'),('\n{','{'),('{\n','{'),('}\n','}'),('\n\[','['),('\n\]',']'),('\[\n','['),('\]\n',']'),(',\n',','),('\n',','),('返回数据',',返回数据')]
for o1,t1 in trans1:
	values_map = map(lambda _:re.sub(o1,t1,_,0,0),list1)
	list1=map2list(values_map)

### 写入数据库
# 建库表
dbname = './interface.db'
innertable = 'innerinterface'
createinnertable = 'create table ' + innertable + '(key int(10) primary key  NOT NULL, value JSON  NOT NULL)'
insertdata = 'insert into `'+ innertable + '` values (?,?)'
innerdata = []
for d1 in range(len(apikeys)):
	innerdata.append((apikeys[d1], list1[d1]))

# 写入数据库
conn = dbapi.get_conn(dbname)
dbapi.drop_table(conn, innertable)
conn = dbapi.get_conn(dbname)
dbapi.create_table(conn, createinnertable)
conn = dbapi.get_conn(dbname)
dbapi.save(conn, insertdata,innerdata)
