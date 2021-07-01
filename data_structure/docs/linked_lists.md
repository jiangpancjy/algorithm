## 链表 Linked List

### 单链表 Single Linked List

![](./img/1.png)

![](./img/2.png)

单链表，也称单向链表 (Single Linked List)，由许多节点连接而成。单个节点由两部分 (value 和 next) 组成，value 用于存储数据，next 用于存储下一个节点的引用 (也可以理解为一个指针，指向下一个节点)。

通常我们会在链表的开头添加一个哨兵节点 (sentinel) 作为伪头 (pseudo-head)，可以简化插入等操作。哨兵节点不计入链表长度，也无法用索引访问。

我们还有一个字段 head，用于存储伪头的引用 (也可以理解成头指针，指向伪头节点)。



#### 链表支持的操作

##### 1. 初始化

我们可以使用以下的代码创建一个空链表：

```python
linked_list = LinkedList()
```

也可以传入一个可迭代对象，将其转换为链表：

```python
linked_list1 = LinkedList([1, 2, 3])
linked_list2 = LinkedList((1, 2, 3))
linked_list3 = LinkedList(range())
```



##### 2. 显示链表信息

当我们打印链表对象时，

```python
print(linked_list)
print(linked_list1)
print(linked_list2)
print(linked_list3)
```

会显示出对应的信息：

```python
【head】
【head】->【1】->【2】->【3】
【head】->【1】->【2】->【3】
【head】->【0】->【1】->【2】->【3】->【4】
```



##### 3. 访问链表元素

我们可以使用索引的方式访问指定下标的元素，

```python
print(linked_list1[0])
```

会得到该链表的第一个元素：

```python
1
```



##### 4. 修改对应元素

我们可以使用索引指定一个元素后，修改其值：

```python
linked_list1[0] = 'hello'
print(linked_list1)
```

输出结果如下所示：

```python
【head】->【hello】->【2】->【3】
```



##### 5. 获取链表长度

我们可以使用 Pyhton 内置方法 `len` 获得链表的长度：

```python
length = len(linked_List1)
print(length)
```

输出结果如下所示：

```python
3
```



##### 6. 迭代

我们可以使用 `for` 语句遍历链表，如下所示：

```python
for node in linked_list1:
    print(node.value)
```

输出结果如下所示：

```python
hello
2
3
```



#### 链表方法

##### 1. append 

**作用**

在链表尾部插入一个节点。

**语法**

```python
linked_list.append(value)
```

**参数**

- value -- 要插入节点的值

**返回值**

无

**实例**

```python
linked_list = LinkedList(range(3))
print(linked_list)
linked_list.append(3)
print(linked_list)
```

**结果**

```python
【head】->【0】->【1】->【2】
【head】->【0】->【1】->【2】->【3】
```



##### 2. insert

**作用**

在链表指定位置 pos 处的节点前插入一个节点。

**语法**

```python
linked_list.insert(pos, value)
```

**参数**

- pos -- 链表中节点的位置
- value -- 要插入节点的值

**返回值**

无

**实例**

```python
linked_list = LinkedList(range(3))
print(linked_list)
linked_list.insert(1, 'hello')
print(linked_list)
```

**结果**

```python
【head】->【0】->【1】->【2】
【head】->【0】->【hello】->【1】->【2】
```



##### 3. remove

**作用**

移除与值匹配的第一个节点。

**语法**

```python
linked_list.remove(value)
```

**参数**

- value -- 要移除节点的值

**返回值**

无

**实例**

```python
linked_list = LinkedList(range(3))
print(linked_list)
linked_list.remove(2)
print(linked_list)
```

**结果**

```python
【head】->【0】->【1】->【2】
【head】->【0】->【1】
```



##### 4. pop

**作用**

移除指定位置的节点并返回，默认移除最后一个节点。

**语法**

```python
linked_list.pop(pos=-1)
```

**参数**

- pos -- 链表中节点的位置

**返回值**

返回移除的节点。

**实例**

```python
linked_list = LinkedList(range(5))
print(linked_list)
print(linked_list.pop().value)
print(linked_list)
print(linked_list.pop(1).value)
print(linked_list)
```

**结果**

```python
【head】->【0】->【1】->【2】->【3】->【4】
4
【head】->【0】->【1】->【2】->【3】
1
【head】->【0】->【2】->【3】
```



### 双链表 Double Linked List

 双链表，也称双向链表 (Double Linked List)，由许多节点组成，每个节点包括存储数据部分，还包括前缀指针 (pre) 指向前一个节点，后缀指针 (next) 指向后一个节点。



![](.\img\3.png)

![](.\img\4.png)

通常我们会在链表的开头添加两个哨兵节点 (sentinel) 作为伪头 (pseudo-head) 和伪尾 (pseudo-tail)，可以简化插入、删除等操作。哨兵节点不计入链表长度，也无法用索引访问。

我们还有两个字段 head 和 tail，用于存储伪头和伪尾的引用 (也可以理解成头指针和尾指针，指向伪头节点和伪尾节点)。

