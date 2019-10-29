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

* 结果为![image-20191029101634108](image-20191029101634108.png)

## 理解