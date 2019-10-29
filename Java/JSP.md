# JSP

`Java Server Pages`在网页中嵌入`Java`代码

## 快速体验

* 新建`index.jsp`

    ```html
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

* 部署服务器后访问 http://localhost:8080/TestCookie/ ![image-20191029213705640](image-20191029213705640.png)

* 与此同时控制台输出![image-20191029213733003](image-20191029213733003.png)

错误页

* 有时



