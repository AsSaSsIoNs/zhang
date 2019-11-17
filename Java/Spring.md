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
        <bean id="accountService" class="com.itheima.service.impl.AccountServiceImpl"></bean>
    </beans><!--</beans>-->
    ```

    

## 