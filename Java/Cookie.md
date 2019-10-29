# Cookie

## 快速体验

* ```java
    @WebServlet(name = "Test1", urlPatterns = "/Test1")
    public class Test1 extends HttpServlet {
        protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
            Cookie cookie = new Cookie("cookie", "testCookie");
            response.addCookie(cookie);
            response.addCookie(new Cookie("hello", "你好"));
        }
        protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
            this.doPost(request, response);
        }
    }//设置了两个Cookie
    ```

    ```java
    @WebServlet(name = "Test2", urlPatterns = "/Test2")
    public class Test2 extends HttpServlet {
        protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
            System.out.println("*******************************************************************");
            Cookie[] cookies = request.getCookies();
            for (Cookie each : cookies) {
                System.out.println(each.getName() + "=" + each.getValue());
            }
        }
        protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
            this.doPost(request, response);
        }
    }//在另外一个页面中提取Cookie的键值对并输出
    ```

* 先访问`localhost:8080/TestCookie/Test1`再访问`localhost:8080/TestCookie/Test2`

* 结果为![image-20191029101634108](image-20191029101634108.png)

## 持久化

* 默认情况下，关闭浏览器Cookie即会被删除

	* 还是上面两个`Servlet`
	* 先访问`localhost:8080/TestCookie/Test1`，再关闭浏览器，再访问`localhost:8080/TestCookie/Test2`
	* 控制台中没有上面的Cookie
	
* 修改Test1.java

    ```java
    @WebServlet(name = "Test1", urlPatterns = "/Test1")
    public class Test1 extends HttpServlet {
        protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
            System.out.println("Hello");
            Cookie cookie = new Cookie("cookie", "testCookie");
            cookie.setMaxAge(20);//设置持续时间
            response.addCookie(cookie);
            response.addCookie(new Cookie("hello", "你好"));
        }
        protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
            this.doPost(request, response);
        }
    }
    ```

* 还是刚才的操作，先访问`localhost:8080/TestCookie/Test1`，再访问`localhost:8080/TestCookie/Test2`，控制台输出为![image-20191029102453244](image-20191029102453244.png)

* 等待20秒后刷新`localhost:8080/TestCookie/Test2`，输出为![image-20191029102610471](image-20191029102610471.png)

* 可以发现，`cookie=testCookie`消失，原因是我们设置了20秒后自动删除，而没有设置自动删除的`cookie`被保留下来，当然如果关闭了浏览器，它也会被删除

* 如果设置`cookie.setMaxAge()`参数为一个很大的值，那么它将会被长时间保留，即使关闭了浏览器也是如此，将其设置为`10000`

* 访问Test1后关闭浏览器再访问Test2，输出为![image-20191029103152278](image-20191029103152278.png)

* 说明这个`Cookie`被持续存储了

## 共享

* 实现两个项目共享一个Cookie

* ```java
    @WebServlet(name = "Test1", urlPatterns = "/Test1")
    public class Test1 extends HttpServlet {
        protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
            System.out.println("Hello");
            Cookie cookie = new Cookie("cookie", "testCookie");
            cookie.setPath("/");
            response.addCookie(cookie);
            response.addCookie(new Cookie("hello", "你好"));
        }
        protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
            this.doPost(request, response);
        }
    }
    ```

    ```java
    @WebServlet(name = "Test2", urlPatterns = "/Test2")
    public class Test2 extends HttpServlet {
        protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
            System.out.println("*******************************************************************");
            Cookie[] cookies = request.getCookies();
            for (Cookie each : cookies) {
                System.out.println(each.getName() + "=" + each.getValue());
            }
        }
        protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
            this.doPost(request, response);
        }
    }
    ```

    



