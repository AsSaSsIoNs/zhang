# JSP

`Java Server Pages`在网页中嵌入`Java`代码

## 快速体验

* 新建`index.jsp`

    ```jsp
    <%@ page contentType="text/html;charset=UTF-8" language="java" %>
    <html>
      <head>
        <title>$Title$</title>
      </head>
      <body>
      $END$
      <%
        System.out.println("Hello");
      %>
      <h1>Hello</h1>
      </body>
    </html>
    ```

* 部署服务器后访问`localhost:8080/TestCookie/`![image-20191029213705640](image-20191029213705640.png)

* 与此同时控制台输出![image-20191029213733003](image-20191029213733003.png)

## 错误页

* 有时访问网页错误时并不想看到报错信息，这时候需要定义`errorPage`属性

* ```jsp
    <%@ page contentType="text/html;charset=UTF-8" language="java" errorPage="ErrorPage.jsp" <%--设置错误页跳转至相应的页面--%>%>
    <html>
      <head>
        <title>$Title$</title>
      </head>
      <body>
      $END$
      <%
        System.out.println("Hello");
        int i = 1 / 0;<%--错误的代码块--%>
      %>
      <h1>Hello</h1>
      </body>
    </html>
    ```

* 同时编写一个`ErrorPage.jsp`文件

    ```jsp
    <%@ page contentType="text/html;charset=UTF-8" isErrorPage="true" language="java" %><%--isErrorPage标记是否为错误页，true时exception对象就可用了--%>
    <html>
    <head>
        <title>错误页面</title>
    </head>
    <body>
        <h1>服务器发生错误</h1>
        <%
            System.out.println(exception.getMessage());//这句话必须在isErrorPage为true时才可用
        %>
    </body>
    </html>
    ```

* 启动服务器访问`localhost:8080/TestCookie/`![image-20191029214243250](image-20191029214243250.png)

* 控制台输出![image-20191029214950020](image-20191029214950020.png)

## EL表达式

用于在`jsp`页面中内嵌代码

* ```jsp
    <%@ page contentType="text/html;charset=UTF-8" language="java" %>
    <html>
        <head>
            <title>TestEL</title>
        </head>
        <body>
            ${1 == 1}
            \${1 == 1}<%--美元加大括号括起来的可执行的一段代码，也可以使用转义字符--%>
            
            <h3>获取User</h3><%--类的存取--%>
            <%
                User user = new User("zhang", 18);
            /*
            	已经定义了User对象，
            	public class User {
        			private String name;
        			private int age;
        			**Getters and Setters**
        			//这种好像也被称为一个JavaBean
        		}
            */
                request.setAttribute("user", user);//将这个数据存储
            %>
            ${requestScope.user.toString()}<br>
            
            <h3>ArrayList</h3><%--ArrayList类型的存取--%>
            <%
                ArrayList<Integer> ints;
                ints = new ArrayList<Integer>();
                ints.add(1);
                ints.add(2);
                ints.add(3);
                request.setAttribute("ints", ints);
            %>
            ${requestScope.ints[0]}
            ${requestScope.ints[1]}
            ${requestScope.ints[2]}<br>
            
            <h3>HashMap</h3><%--HashMap类型的存取--%>
            <%
                HashMap hashMap = new HashMap();
                hashMap.put("name", "li");
                hashMap.put("age", 11);
                request.setAttribute("hashMap", hashMap);
            %>
            ${requestScope.hashMap.name}
            ${requestScope.hashMap["age"]}
            
            <h3>empty运算符</h3><%--empty运算符--%>
            <%
                String string1 = "test";
                String string2 = null;
                request.setAttribute("string1", string1);
                request.setAttribute("string2", string2);
            %>
            ${requestScope.string1}
            ${requestScope.string2}<br>
            ${empty string1}
            ${empty string2}
            
            <h3>pageContext</h3><%--内置对象pageContext--%>
            ${pageContext.request.contextPath}<br>
        </body>
    </html>
    ```

* 



