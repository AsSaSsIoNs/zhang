# Spring

非常成熟的框架，降低耦合

## 搭建环境

*   新建Maven白板工程，编辑pom文件导入spring-context

*   创建service层的接口与实现类

    ```java
    public interface AccountService {
        void saveAccount();
    }
    
    public class AccountServiceImpl implements AccountService {
        public AccountServiceImpl() {
            System.out.println("创建了AccountServiceImpl...");
        }
        public void saveAccount() {
            System.out.println("saveAccount...");
        }
    }
    ```

*   ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <beans xmlns="http://www.springframework.org/schema/beans"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://www.springframework.org/schema/beans
            http://www.springframework.org/schema/beans/spring-beans.xsd">
        <bean id="accountService" class="com.itheima.service.impl.AccountServiceImpl"></bean><!--指定实现类，并给一个id用来标明新建的类id-->
    </beans>
    ```

*   ```java
        @Test
        public void test1(){
            ApplicationContext ac = new ClassPathXmlApplicationContext("bean.xml");
            AccountService accountService = (AccountService) ac.getBean("accountService");
            System.out.println(accountService);
        }/*结果是
        创建了AccountServiceImpl...
    com.itheima.service.impl.AccountServiceImpl@305fd85d*/
    ```

    

## 创建Bean

三种方式来创建Bean

### 构造方法

```java
    public AccountServiceImpl() {
        System.out.println("创建了AccountServiceImpl...");
    }/*AccountService类中追加的无参构造*/
/*xml文件保持原样*/
```

```java
    @Test
    public void test2(){
        ApplicationContext ac = new ClassPathXmlApplicationContext("bean.xml");
        AccountService accountService = (AccountService) ac.getBean("accountService");
    }/*结果为
    创建了AccountServiceImpl...*/
```

### InstanceFactory

```java
public class InstanceFactory {
    public AccountService getAccountService(){
        System.out.println("执行了InstanceFactory");
        return new AccountServiceImpl();
    }
}/*这个不是真正的Factory，只是用来模拟*/
```

```xml
    <bean id="instanceFactory" class="com.itheima.factory.InstanceFactory"></bean>
    <bean id="accountService" factory-bean="instanceFactory" factory-method="getAccountService"></bean><!--指定了先创建InstanceFactory,再通过这个工程来创建，标签用来指定是哪个工厂，以及创建Bean的方法-->
```

```java
    @Test
    public void test2(){
        ApplicationContext ac = new ClassPathXmlApplicationContext("bean.xml");
        AccountService accountService = (AccountService) ac.getBean("accountService");
    }/*结果为
    执行了InstanceFactory
	创建了AccountServiceImpl...*/
```

### StaticFactory

```java
public class StaticFactory {
    public static AccountService getAccountService(){
        System.out.println("执行了StaticFactory");
        return new AccountServiceImpl();
    }
}
```

```xml
 <bean id="accountService" class="com.itheima.factory.StaticFactory" factory-method="getAccountService"></bean><!--静态工厂不需要手动创建-->
```

```java
    @Test
    public void test2(){
        ApplicationContext ac = new ClassPathXmlApplicationContext("bean.xml");
        AccountService accountService = (AccountService) ac.getBean("accountService");
    }/*结果为
    执行了StaticFactory
	创建了AccountServiceImpl...*/
```

## 依赖注入

将对象的创建交给Spring

### 构造函数注入


```java
public class AccountServiceImpl implements AccountService {
        private String name;
        private Integer age;
        private Date birthday;
        public void saveAccount() {
            System.out.println("saveAccount...");
        }
        /*Constructor toString*/
    }
    public interface AccountService {
        void saveAccount();
    }
```

```xml
<bean id="accountService" class="com.itheima.service.impl.AccountServiceImpl">
        <constructor-arg name="name" value="test"></constructor-arg>
        <constructor-arg name="age" value="13"></constructor-arg>
        <constructor-arg name="birthday" ref="now"></constructor-arg>
    </bean><!--标签指定了要创建的对象，以及他的id，而constructor-arg标签则指定了他们构造函数要创建的内容，使用name-value对来确定初始化哪个属性，其中，date因为需要转换而使用了ref标签，ref类型为其他Bean类型，需要注明id-->
<bean id="now" class="java.util.Date"></bean>
```

```java
@Test
public void testSDI(){
    accountService = (AccountService) applicationContext.getBean("accountService");
    accountService.saveAccount();
    System.out.println(accountService.toString());
}/*
        saveAccount...
    AccountServiceImpl{name='test', age=13, birthday=Sun Nov 17 11:09:49 CST 2019}*/
```

### set注入

```java
public class AccountServiceImpl2 implements AccountService {
    private String name;
    private Integer age;
    private Date birthday;
    public void saveAccount() {
    }
    /*toString Setters*/
}
```

```xml
    <bean id="accountService2" class="com.itheima.service.impl.AccountServiceImpl2">
        <property name="name" value="张一"></property>
        <property name="age" value="13"></property>
        <property name="birthday" ref="now"></property>
    </bean>
```

```java
    @Test
    public void testSetter(){
        accountService = (AccountService) applicationContext.getBean("accountService2");
        System.out.println(accountService);
    }/*AccountServiceImpl2{name='张一', age=13, birthday=Sun Nov 17 11:20:39 CST 2019}*/
```



### 注入集合

```java
public class AccountServiceImpl3 implements AccountService {
    private String[] myStrs;
    private List<String> myList;
    private Set<String> mySet;
    private Map<String, String> myMap;
    private Properties myProps;
    public void saveAccount() {
    }
    /*Getters Setters toString*/
```

```xml
<bean id="accountService3" class="com.itheima.service.impl.AccountServiceImpl3">
        <property name="myStrs">
            <set>
                <value>AAA</value>
                <value>BBB</value>
                <value>CCC</value>
            </set>
        </property>
        <property name="myList">
            <array>
                <value>AAA</value>
                <value>BBB</value>
                <value>CCC</value>
            </array>
        </property>
        <property name="mySet">
            <list>
                <value>AAA</value>
                <value>BBB</value>
                <value>CCC</value>
            </list>
        </property>
        <property name="myMap">
            <props>
                <prop key="testC">ccc</prop>
                <prop key="testD">ddd</prop>
            </props>
        </property>
        <property name="myProps">
            <map>
                <entry key="testA" value="aaa"></entry>
                <entry key="testB" value="BBB"></entry>
            </map>
        </property>
    </bean>
```

