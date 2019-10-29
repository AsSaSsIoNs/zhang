# Cookie

## 快速体验

* ```java
    @WebServlet(name = "Test1", urlPatterns = "/Test1")
    public class Test1 extends HttpServlet {
        protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
            System.out.println("Hello");
            Cookie cookie = new Cookie("cookie", "testCookie");
            response.addCookie(cookie);
            response.addCookie(new Cookie("hello", "你好"));
        }
        protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
            this.doPost(request, response);
        }
    }
    ```

    ```
    
    ```

    