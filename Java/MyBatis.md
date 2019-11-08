# MyBatis

方便地进行数据库读写

*   新建`Maven`白板工程

*   编辑`pom.xml`文件，导入包

    ```xml
    <dependencies>
            <dependency>
                <groupId>org.mybatis</groupId>
                <artifactId>mybatis</artifactId>
                <version>3.4.5</version>
            </dependency>
            <dependency>
                <groupId>mysql</groupId>
                <artifactId>mysql-connector-java</artifactId>
                <version>5.1.32</version>
            </dependency>
            <dependency>
                <groupId>log4j</groupId>
                <artifactId>log4j</artifactId>
                <version>1.2.17</version>
            </dependency>
            <dependency>
                <groupId>junit</groupId>
                <artifactId>junit</artifactId>
                <version>4.12</version>
            </dependency>
        </dependencies>
    ```

    主要是`mybatis` \ `mysqlconnector` \ `junit` \ `log4j`四个包

*   `./src/main/java/com/zhang/domain/`建立`User`类

    ```java
    package com.zhang.domain;
    public class User {
        private Integer id;
        private String username;
        private Date birthday;
        private String sex;
        private String address;
        /*Getters Setters toString*/
    }
    ```

*   `./src/main/resources/`下建立`SqlMapConfig.xml`文件配置连接

    ```xml
    <configuration>
        <environments default="mysql">
            <environment id="mysql">
                <transactionManager type="JDBC"></transactionManager>
                <dataSource type="POOLED">
                    <property name="driver" value="com.mysql.jdbc.Driver"/>
                    <property name="url" value="jdbc:mysql://localhost:3306/test"/>
                    <property name="username" value="root"/>
                    <property name="password" value=""/>
                </dataSource>
            </environment>
        </environments>
        <mappers>
            <mapper resource="com/zhang/dao/UserDao.xml"/><!--指示查询配置文件的位置-->
        </mappers>
    </configuration>
    ```

*   `./src/main/resources/com/zhang/dao`下建立`UserDao.xml`,设置查询

    ```xml
    <mapper namespace="test"><!--设置命名空间-->
        <select id="findAll" resultType="com.zhang.domain.User"><!--resultType设置查询后要返回的对象-->
            select * from user
        </select>
        <select id="SelectById" parameterType="int" resultType="com.zhang.domain.User"><!--parameterType设置为查询参数的类型-->
            select * from user where id=#{value}
        </select>
        <select id="SelectByUsername" parameterType="String" resultType="com.zhang.domain.User">
            select * from user where username like '%${value}%'
        </select>
    </mapper>
    ```

*   `./src/test/java/`建立单元测试类`TestMyBatis`

    ```java
    public class TestMyBatis {
        @Test
        public void testSelectAll() throws Exception{
            String resource = "SqlMapConfig.xml";
            InputStream resourceAsStream = Resources.getResourceAsStream(resource);
            SqlSessionFactory build = new SqlSessionFactoryBuilder().build(resourceAsStream);
            SqlSession sqlSession = build.openSession();
            List<Object> objects = sqlSession.selectList("test.findAll");//命名空间+方法名
            for (Object each : objects) {
                System.out.println(each);
            }
            sqlSession.close();
            resourceAsStream.close();
        }
    /*已经测试过*/
        @Test
        public void testSelectById() throws Exception{
            String resource = "SqlMapConfig.xml";
            InputStream resourceAsStream = Resources.getResourceAsStream(resource);
            SqlSessionFactory build = new SqlSessionFactoryBuilder().build(resourceAsStream);
            SqlSession sqlSession = build.openSession();
            List<Object> objects = sqlSession.selectList("test.SelectById", 50);//命名空间+方法名，加上参数
            for (Object each : objects) {
                System.out.println(each);
            }
            sqlSession.close();
            resourceAsStream.close();
        }
        /*
        User{id=50, username='张一', birthday=Mon Nov 04 00:00:00 CST 2019, sex='男', address='西安'}
        */
        @Test
        public void testSelectByUsername() throws Exception{
            String resource = "SqlMapConfig.xml";
            InputStream resourceAsStream = Resources.getResourceAsStream(resource);
            SqlSessionFactory build = new SqlSessionFactoryBuilder().build(resourceAsStream);
            SqlSession sqlSession = build.openSession();
            List<Object> objects = sqlSession.selectList("test.SelectByUsername", "张");//经过测试，命名空间可以随意设置，目的是分开可能重名的方法
            for (Object each : objects) {
                System.out.println(each);
            }
            sqlSession.close();
            resourceAsStream.close();
        }
        /*
        User{id=50, username='张一', birthday=Mon Nov 04 00:00:00 CST 2019, sex='男', address='西安'}
    User{id=51, username='张二', birthday=Mon Nov 04 00:00:00 CST 2019, sex='女', address='西安'}
        */
    }
    ```
    
    *   解决User类属性和数据库列名不一致的匹配问题