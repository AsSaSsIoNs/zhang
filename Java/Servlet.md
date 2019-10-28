# Servlet

*运行在服务器上的Java程序*

------



## 快速体验

- 安装好Tomcat与IDEA

- 新建JAVA Enterprise工程

- 选择Web Application

- 建好后的目录./src下建立一个ServletDemo.java

    ```java
    import javax.servlet.*;
    import java.io.IOException;
    
    public class ServletDemo implements Servlet {
        @Override
        public void init(ServletConfig servletConfig) throws ServletException {
        }
    
        @Override
        public ServletConfig getServletConfig() {
            return null;
        }
    
        @Override
        public void service(ServletRequest servletRequest, ServletResponse servletResponse) throws ServletException, IOException {
            System.out.println("SSSSSSEEEEERVVVVVVLEEEET");
        }
    
        @Override
        public String getServletInfo() {
            return null;
        }
    
        @Override
        public void destroy() {
    
        }
    }
    
    ```

    

    也就是实现一个Servlet接口，但是仅实现service方法

- 后来编辑./web/WEB-INF/web.xml

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"
             version="3.1">
        <servlet>
            <servlet-name>demo1</servlet-name>
            <servlet-class>ServletDemo</servlet-class>
        </servlet>
        <servlet-mapping>
            <servlet-name>demo1</servlet-name>
            <url-pattern>/demo1</url-pattern>
        </servlet-mapping>
    </web-app>
    ```

    注意servlet-class标签内容应与自定义的类名相同，url-pattern标签即指定了此页面的访问地址

- 点击运行Tomcat服务器，看到了这个页面![1571140384807](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1571140384807.png)

- 访问/demo1，发现什么内容都没有，这就表示成功。因为如果出错会出现404界面。同时控制台出现![1571140495503](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1571140495503.png)

    也就是上面ServletDemo.service方法里面定义的内容

- 浏览器访问页面时确实触发了service方法，每一次访问都会调用一次

- 这里可以修改项目在url中的定位，比如改成"/"，就表示localhost:8080即可定位至index.jsp,如果这样修改，那么我们自己定义的Servlet的路径就变成了localhost:8080/demo1<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1571140863404.png" style="zoom: 50%;" />

## Servlet生命周期

- 在./src下再建一个ServletDemo2.java，这个类中，实现了init、service和destroy方法

    ```java
    import javax.servlet.*;
    import java.io.IOException;
    
    public class ServletDemo2 implements Servlet {
        @Override
        public void init(ServletConfig servletConfig) throws ServletException {
            System.out.println("执行init方法");
        }
    
        @Override
        public ServletConfig getServletConfig() {
            return null;
        }
    
        @Override
        public void service(ServletRequest servletRequest, ServletResponse servletResponse) throws ServletException, IOException {
            System.out.println("执行service方法");
        }
    
        @Override
        public String getServletInfo() {
            return null;
        }
    
        @Override
        public void destroy() {
            System.out.println("执行destroy方法");
        }
    }
    ```

- 编辑./web/WEB-INF/web.xml，做到标签之间的对应

    ```xml
    <servlet>
            <servlet-name>demo2</servlet-name>
            <servlet-class>ServletDemo2</servlet-class>
        </servlet>
        <servlet-mapping>
            <servlet-name>demo2</servlet-name>
            <url-pattern>/demo2</url-pattern>
        </servlet-mapping>
    ```

- 开启Tomcat服务器，并访问 http://localhost:8080/LearnServlet_war_exploded/demo2 ，期间多次刷新页面，当然页面肯定是什么都没有的，最后关闭服务器，控制台的内容如下![1571142133558](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1571142133558.png)![1571142159675](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1571142159675.png)

- init只在创建Servlet时执行一次，service会在每次访问时执行，destroy则会在服务器关闭、Servlet销毁时执行

### 控制Servlet的创建时机

在的./web/WEB-INF/web.xml中找到刚才定义的Servlet标签，加入下面一行

```xml
        <load-on-startup>5</load-on-startup>
```

再运行Tomcat服务器，控制台输出是这样的![1571142728575](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1571142728575.png)

init方法在服务器初始化之前就执行了

- 这个load-on-startup值为正数时init方法就在初始化之前执行

## 使用注解特性

配置一个Servlet需要实现接口以及设置xml文件，要注意名字必须对应，显得非常麻烦，注解特性就很好地解决了这个问题

- 新建一个Java Enterprise项目，在创建Web Application时把create web.xml选项取消![1571143449629](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1571143449629.png)

    建立之后，./web目录下自然没有web.xml文件了

- ./src/下新建TestAnnotation.java

    ```java
    import javax.servlet.*;
    import javax.servlet.annotation.WebServlet;
    import java.io.IOException;
    @WebServlet(urlPatterns = "/demo")
    public class TestAnnotation implements Servlet {
        @Override
        public void init(ServletConfig servletConfig) throws ServletException {
            System.out.println("测试注解特性");
        }
    
        @Override
        public ServletConfig getServletConfig() {
            return null;
        }
    
        @Override
        public void service(ServletRequest servletRequest, ServletResponse servletResponse) throws ServletException, IOException {
    
        }
    
         @Override
        public String getServletInfo() {
            return null;
        }
    
        @Override
        public void destroy() {
    
        }
    }
    ```

    可以看到，在TestAnnotation类之前的@WebServlet(urlPatterns = "/demo")，正是设置了这个Servlet的url

- 运行Tomcat服务器，访问 http://localhost:8080/TestAnnotation_war_exploded/demo ，控制台如下显示![1571143894763](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1571143894763.png)

- 成功地使用了注解特性

## GenericServlet和HttpServlet

上面实现的Servlet必须要实现五个方法，有时候只能空着，而这两中Servlet就解决了这些问题

- ./src/下新建两个类TestGenericServlet和TestHttpServlet

    ```java
    import javax.servlet.GenericServlet;
    import javax.servlet.ServletException;
    import javax.servlet.ServletRequest;
    import javax.servlet.ServletResponse;
    import javax.servlet.annotation.WebServlet;
    import java.io.IOException;
    
    @WebServlet(urlPatterns = "/TestGenericServlet")
    public class TestGenericServlet extends GenericServlet {
        @Override
        public void service(ServletRequest servletRequest, ServletResponse servletResponse) throws ServletException, IOException {
            System.out.println("TestGenericServlet.service()");
        }
    }
    ```

    ```java
    import javax.servlet.ServletException;
    import javax.servlet.annotation.WebServlet;
    import javax.servlet.http.HttpServlet;
    import javax.servlet.http.HttpServletRequest;
    import javax.servlet.http.HttpServletResponse;
    import java.io.IOException;
    
    @WebServlet(urlPatterns = "/TestHttpServlet")
    public class TestHttpServlet extends HttpServlet {
        @Override
        protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
            System.out.println("TestHttpServlet.doGet()");
        }
    
        @Override
        protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
            System.out.println("TestHttpServlet.doPost()");
        }
    }
    ```

- 可以看到不同于实现Servlet接口，两个类都继承了要测试的类

- 测试TestHttpServlet.doPost方法，在./web/下建立一个TestHttpServlet_doPost.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>TestHttpServlet_doPost()</title>
    </head>
    <body>
        <form action="/TestHttpServlet" method="post">
            <input name="username">
            <input type="submit" value="提交">
        </form>
    </body>
    </html>
    ```

- 运行Tomcat服务器，访问 http://localhost:8080/TestGenericServlet 与 http://localhost:8080/TestHttpServlet ，控制台输出如下语句![1571190643534](J:\我的坚果云\Note\Java\1571190643534.png)

- 访问 http://localhost:8080/TestHttpServlet_doPost.html ，填写任意内容并提交表单![1571190758579](J:\我的坚果云\Note\Java\1571190758579.png)控制台输出如下![1571190816021](J:\我的坚果云\Note\Java\1571190816021.png)

- 即访问TestGenericServlet时触发service方法，访问TestHttpServlet时触发doGet方法，提交内容时触发doPost方法

## 设置urlpattern

观察urlpattern属性的源码就会发现，这个属性接受一个数组，所以下面测试一下一个Servlet能不能接受多个路径访问

- ./src/下新建一个TestMultiUrlPatterns类

    ```java
    @WebServlet(urlPatterns = {"/test1", "/test2", "/test3"})
    public class TestMultiUrlPatterns extends HttpServlet {
        @Override
        protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
            System.out.println("TestMultiUrlPatterns.doGet");
        }
    }
    ```

    观察到第一行中urlPatterns接收了一个数组

- 启动服务器依次访问 http://localhost:8080/test1、http://localhost:8080/test2、http://localhost:8080/test3，控制台输出如下

- ![1571191643648](J:\我的坚果云\Note\Java\1571191643648.png)

- 也就是使用了三个url访问到了同一个Servlet

    ### 使用通配符

    - ./src/下新建一个TestWildcards类

        ```java
        @WebServlet(urlPatterns = "/*")
        public class TestWildcards extends HttpServlet {
            @Override
            protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
                System.out.println("TestWildcards.doGet");
            }
        }
        ```

    - 启动服务器，访问（localhost:8080/+任意内容）若干次，控制台输出下面内容

    - ![1571191949037](J:\我的坚果云\Note\Java\1571191949037.png)

        

## Http协议

- 运行服务器，访问 http://localhost:8080/TestHttpServlet_doPost.html ，按f12进入控制台

- ![1571192908757](J:\我的坚果云\Note\Java\1571192908757.png)

- 可以看到请求网址，请求方法，状态码等信息

- 填写内容并提交，再进入控制台

- ![1571192966030](J:\我的坚果云\Note\Java\1571192966030.png)

- 发现如下信息，正是在html页面中定义的参数

    ### doGet与doPost

    - 编辑./web/TestHttpServlet_doPost.html文件，将form标签的method属性改为“get”

    - 再次提交表单，发现url变为了这样

    - ![1571193177112](J:\我的坚果云\Note\Java\1571193177112.png)

        *doGet方法会把请求参数放到url中，而doPost却不会*

# Request和Response

输出HttpServletRequest对象的信息，System输出对象信息

org.apache.catalina.connector.RequestFacade@6e70f6c0

这个类实现了HttpServletRequest接口

## Request获取请求头

### 测试request的方法输出

- 实现TestRequest类

- ```java
    System.out.println("getMethod()" + "\t\t" + req.getMethod());
            System.out.println("getContextPath()" + "\t\t" + req.getContextPath());
            System.out.println("getServletPath()" + "\t\t" + req.getServletPath());
            System.out.println("getQueryString()" + "\t\t" + req.getQueryString());
            System.out.println("getRequestURI()" + "\t\t" + req.getRequestURI());
            System.out.println("getRequestURL()" + "\t\t" + req.getRequestURL());
            System.out.println("getProtocol()" + "\t\t" + req.getProtocol());
            System.out.println("getRemoteAddr()"+ "\t\t" + req.getRemoteAddr());
    ```

- 访问 http://localhost:8080/TestRequest?name=zhang&age=22 ，这个url中附带了请求参数

- ```
    getMethod()		GET
    getContextPath()		
    getServletPath()		/TestRequest
    getQueryString()		name=zhang&age=22
    getRequestURI()		/TestRequest
    getRequestURL()		http://localhost:8080/TestRequest
    getProtocol()		HTTP/1.1
    getRemoteAddr()		0:0:0:0:0:0:0:1
    ```

    可以得到相应的信息，比如协议名、请求方法、请求参数、Servlet路径等等

### 测试getHeaderNames

- 实现TestRequest2类

- ```java
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
            Enumeration<String> headers = req.getHeaderNames();
            while (headers.hasMoreElements()){
                String name = headers.nextElement();
                String value = req.getHeader(name);
                System.out.println(name + "::::::" + value);
            }
        }
    ```

- <img src="J:\我的坚果云\Note\Java\1571212212502.png" alt="1571212212502" style="zoom:50%;" />

- 从输出看返回了所有的请求名以及对应值

### 小demo

- 判断使用的浏览器是不是Chrome，实现TestRequest3类

- ```java
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
            String agent = req.getHeader("user-agent");
            if(agent.contains("Chrome")){
                System.out.println("使用Chrome访问了");
            }else{
                System.out.println("不是Chrome");
            }
        }
    ```

- 启动后分别使用Chrome和IE访问 http://localhost:8080/TestRequest3 ，控制台输出如下

- ![1571212681596](J:\我的坚果云\Note\Java\1571212681596.png)

- 当然还可以判断Firefox还有Safari等浏览器，懒得下就这样吧

## Request获取请求体

编写TestRequest4类测试

- ```java
    @WebServlet(urlPatterns = "/TestRequest4")
    public class TestRequest4 extends HttpServlet {
        @Override
        protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
            BufferedReader br = req.getReader();
            String line = null;
            while ((line = br.readLine()) != null){
                System.out.println(line);
            }
        }
    }
    ```

- ./web/下新建TestRequest4.html文件

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>TestRequest4</title>
    </head>
    <body>
        <form action="/TestRequest4" method="post">
            <input type="text" placeholder="输入框" name="DATADATA">
            <input type="submit" value="提交">
        </form>
    </body>
    </html>
    ```

- 访问 http://localhost:8080/TestRequest4.html ,填写数据并点击提交按钮，控制台输出如下![1571214250326](J:\我的坚果云\Note\Java\1571214250326.png)

    ### 接受请求参数

    - 新建TestRequest5类与TestRequest5.html用来测试

    - ```java
        public class TestRequest5 extends HttpServlet {
            @Override
            protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
                Map<String, String[]> parameters = req.getParameterMap();
                Set<String> keyset = parameters.keySet();
                for (String key : keyset) {
                    String[] values = parameters.get(key);
                    System.out.println(key);
                    for (String value : values) {
                        System.out.println(value);
                    }
                }
            }
            @Override
            protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
                super.doGet(req, resp);
            }
        }
        ```

    - ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>TestRequest5</title>
        </head>
        <body>
            <form action="/TestRequest5" method="get">
                <input type="text" name="Data1"><br>
                <input type="text" name="Data1"><br>
                <input type="submit" value="提交">
            </form>
        </body>
        </html>
        ```

    - 访问 http://localhost:8080/TestRequest5.html 填写表单提交，控制台输出如下![1571215918203](J:\我的坚果云\Note\Java\1571215918203.png)

    - 使用了Map来承接所有的参数，参数的值可以是一个数组
    
        ### 

