```java
        int a = 1;
        int b = a;
        a = 2;
        System.out.println(a);//2
        System.out.println(b);//1
        TT t = new TT("T");
        TT t1 = t;
        t.setName("TT");
        System.out.println(t.getName());//TT
        System.out.println(t1.getName());//TT
/*
a值为1，b值为a值，也是1
但是a修改为2后，b值保持不变
t为"T",t1为t也为"T",修改t值后t1值却变了，为什么？
	Java的原始类型变量，会直接存储到栈中，因为他们比较简单，而对于类，会存储到堆中
	int a = 1;			在栈中寻找是否存有1这个值的地址，如果没有就新建1，将地址给a
    int b = a;			将a的地址给b，也就是将1的地址给b
    a = 2;				在栈中寻找是否存有2这个值的地址，如果没有就新建2，将地址给a
    					至此，a的地址变化了，由1的地址变为2的地址，但这个过程没有修改b的地址
    TT t = new TT("T");	堆中新建一个对象，其成员变量为"T"，t将其引用
    TT t1 = t;			t1引用的值被设置为t，也就是上句新建的那个对象
    t.setName("TT");	改变t的内容
    					至此，t的内容为"TT"，但是为何t1也为"TT"，因为t1为一个引用变量，值为着t指向的那个对象，所以访问t1时，会访问到那个对象，那个对象以前值的确是"T"，但是在第三句被改成了"TT"，所以t1的getName()也为"TT"了
*/
```



```java
        String a;
        String b = null;
        System.out.println(a);
        System.out.println(b);
/*
第1行的a是一个引用吗？
	其实不是，必须要有对象才能谈引用，好像必须有那个人才能有哪个名字一样
第1行的a值为null吗？
    第1行给人的感觉好像a的值是null，但一对比第2行就发现其实不是，而且第1行连编译都报错
    其实a的值为undefined，这个是和null不同的
*/
```

```java
        String zhangsan, lisi;
        zhangsan = new String("我是对象张三");
        lisi = new String("我是对象李四");
        zhangsan = lisi;//lisi指向的对象地址赋予给了zhangsan，所以指向同一个对象
        System.out.println(zhangsan == lisi);
/*
这样的话zhangsan和lisi才指向了同一个对象
*/
```

```java
        int i = 520, j = 521;//i引用栈中的520 j引用栈中的521
        System.out.println("boy=" + i + "，girl=" + j);//那当然不同了
        i = j;//i的值被j修改，i引用了521
        i = 250;//i的值再次被修改，i引用了250
        System.out.println("boy=" + i + "，girl=" + j);//当然也不同
////////////////////////////////////////////////////////////////////////////
        Lover boy = new Lover();
        boy.level = 520;
        Lover girl = new Lover();
        girl.level = 521;//boy和girl都引用着各自的对象，他们的引用变量值是不一样的
        System.out.println("boy=" + boy.level + "，girl=" + girl.level);
        boy = girl;//boy被修改为，girl引用的对象上了
        girl.level = 250;//修改girl引用的那个对象上的成员变量值
        System.out.println("boy=" + boy.level + "，girl=" + girl.level);//此时boy和girl都引用着同一个变量，不管怎么修改，值都是一样的
/*
上面的为
boy=520，girl=521
boy=250，girl=521
下面的为
boy=520，girl=521
boy=250，girl=250
*/
```

```java
/*主动使用类
*创建这个类的实例
*访问类或接口的静态变量，或对其赋值
*反射
*初始化这个类的子类
*jvm启动时被标明为启动类的类
*动态语言支持
*/
public class MyTest1 {
    public static void main(String[] args) {
		/*
		System.out.println(Father.str1);
		结果为
		Father.static
		Father
		使用了Father,是父类，str1是父类的成员，没有使用Child字类的任何部分，故不对Child类进行初始化，没有运行Child类的static代码块
		System.out.println(Child.str1);
		结果为
		Father.static
		Father
		明明使用了Child类，为什么和上面的还是一样呢?
		其实这个Child.str1并没有使用Child类，str1依然是Father的成员，故对Father进行初始化，不牵扯到Child
		System.out.println(Child.str2);
		结果为
		Father.static
		Child.static
		Child
		使用Child2的成员str2时，要先对其父类做出初始化，所以先有Father.static，再有其他
		*/
    }
}
class Father{
    public static String str1 = "Father";
    static {
        System.out.println("Father.static");
    }
}
class Child extends Father{
    public static String str2 = "Child";
    static {
        System.out.println("Child.static");
    }
}
```

```java
public class MyTest2 {
    public static void main(String[] args) {
        System.out.println(Father1.str1);
        System.out.println("---------------");
        System.out.println(Father2.str1);
        System.out.println("---------------");
        System.out.println(Father3.str1);/*
        Father1.static
        java
        ---------------
        java
        ---------------
        Father3.static
        92b10638-9189-4ca1-a47c-111332074990
        可以看到，差别在于final关键字，如果str1被final所修饰，那么它直接会被放进MyTest2的常量池中，和Father2类没有任何关系，甚至在运行时我们删除了Father2的class文件，这个程序还是可以正常运行
        常量在编译阶段就会存入调用这个常量的方法所在的类的常量池中
        但是在为什么Father3的静态块也运行了呢
        因为即使它的str1变量被final修饰，但是其值是调用随机数，要等到运行时才能确定值，而不是像上面的在编译期就确定好了。同样，删除这个类的class文件，运行时会抛出异常ClassNotFoundException
        */
    }
}

class Father1{
    public static String str1 = "java";
    static {
        System.out.println("Father1.static");
    }
}
class Father2{
    public static final String str1 = "java";
    static {
        System.out.println("Father2.static");
    }
}
class Father3{
    public static final String str1 = UUID.randomUUID().toString();
    static {
        System.out.println("Father3.static");
    }
}
```



```java
public class MyTest3 {
    public static void main(String[] args) {
        Test[] tests = new Test[3];
        System.out.println(tests.getClass());
        int[] ints = new int[2];
        char[] chars = new char[2];
        int[][] ints1 = new int[2][2];
        System.out.println(ints.getClass());
        System.out.println(chars.getClass());
        System.out.println(ints1.getClass());
    }
}
class Test{
    static {
        System.out.println("Test.static");
    }
}
```

