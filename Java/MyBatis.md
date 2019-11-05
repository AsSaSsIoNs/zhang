# MyBatis

方便地进行数据库读写

*   新建Maven白板工程

*   编辑pom.xml文件，导入包

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

    主要是mybatis\mysqlconnector\junit\log4j四个包

*   ./src/main/java/com/zhang/domain/建立User类

    ```java
    package com.zhang.domain;
    public class User {
        private Integer id;
        private String username;
        private Date birthday;
        private String sex;
        private String address;
    }
    ```

*   ./src/main/resources/下建立SqlMapConfig.xml文件配置连接

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
            <mapper resource="com/zhang/dao/UserDao.xml"/>
        </mappers>
    </configuration>
    ```

*   ./src/main/resources/com/zhang/dao下建立UserDao.xml,设置查询

    ```xml
    <mapper namespace="test">
        <select id="findAll" resultType="com.zhang.domain.User">
            select * from user
        </select>
        <select id="SelectById" parameterType="int" resultType="com.zhang.domain.User">
            select * from user where id=#{value}
        </select>
        <select id="SelectByUsername" parameterType="String" resultType="com.zhang.domain.User">
            select * from user where username like '%${value}%'
        </select>
    </mapper>
    ```

*   ./src/test/java/建立单元测试类TestMyBatis

    ```java
    public class TestMyBatis {
        @Test
        public void testSelectAll() throws Exception{
            String resource = "SqlMapConfig.xml";
            InputStream resourceAsStream = Resources.getResourceAsStream(resource);
            SqlSessionFactory build = new SqlSessionFactoryBuilder().build(resourceAsStream);
            SqlSession sqlSession = build.openSession();
            List<Object> objects = sqlSession.selectList("test.findAll");
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
            List<Object> objects = sqlSession.selectList("test.SelectById", 50);
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
            List<Object> objects = sqlSession.selectList("test.SelectByUsername", "张");
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

    

*   