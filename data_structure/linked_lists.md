## 链表

### 单链表

#### 1. 链表的创建

创建空链表

```python
linked_list = LinkedList()
```

初始化一个链表

```python
linked_list = LinkedList([1, 2, 3])
# 或者
linked_list = LinkedList('123')
```

> 注意传入的参数需要是一个序列类型



#### 2. 访问链表元素

可以采用索引的方式访问链表元素

```python
elem = linked_list[1]
```



#### 3. 修改链表元素

```python
linked_list[1] = 'hello'
```



#### 4. 获取链表长度

```python
length = len(linked_list)
```



#### 5. 链表方法

- append
- insert

