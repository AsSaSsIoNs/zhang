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

*   

## 