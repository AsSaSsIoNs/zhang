
# JDBC

>   在Java中执行数据库语句
---

## 快速实现一个

* 下载并导入Connector，此时注意要和安装的mysql版本对应，之前不对应的话就会报错 

* 在`./`下新建一个`libs`文件夹，用来放置connector的包，在`libs`上右键选择`Add as library`

* `./src`下新建测试类`Demo1.java`

* ```java
    public class Demo1 {
        public static void main(String[] args) throws ClassNotFoundException, SQLException {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/test?useSSL=false&serverTimezone=UTC", "root", "");
            //参考网络上的8.0连接方法
            //需要设置useSSL和serverTimezone参数
            String sql = "select * from dept";
            //test数据库是有数据的，故本次查询返回的就是查询成功与否
            Statement stmt = conn.createStatement();
            boolean count = stmt.execute(sql);
            System.out.println(count);
            stmt.close();
            conn.close();
        }
    }
    ```

* 控制台输出![1571367607557](1571367607557.png)

---
## DriverManager

* ```java
  //注册驱动
  static {
        try {
            DriverManager.registerDriver(new Driver());
        } catch (SQLException var1) {
            throw new RuntimeException("Can't register driver!");
        }
    }
  //观察`mysql-connector-java-8.0.11\com\mysql\cj\jdbc\Driver.java`的源码就会发现，每次`DriverManager`强制运行`registerDriver`方法
  ```

* ```java
	// 获取mysql连接
	//如果要连接本机的3306时，可以省略不写
  Connection conn = DriverManager.getConnection("jdbc:mysql:///test?useSSL=false&serverTimezone=UTC", "root", "");
  //Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/test?useSSL=false&serverTimezone=UTC", "root", "");
  //以上两个的执行效果一样
  ```
## ResultSet

*   使用ResultSet输出数据库中的结果

*   ```java
    public static void main(String[] args) throws ClassNotFoundException, SQLException {
            Connection conn = DriverManager.getConnection("jdbc:mysql:///test?useSSL=false&serverTimezone=UTC", "root", "");
            String sql = "select * from dept";
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
            rs.next();
            System.out.println(rs.getString("loc"));
            stmt.close();
            conn.close();
        }
    ```

*   要查询的表是这样的

*   |id|dname|loc
*   |



