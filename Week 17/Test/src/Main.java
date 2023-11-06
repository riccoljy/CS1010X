public class Main {
    public static void main(String[] args) {
        Complex test = new ComplexCart(3,4);
        test.divides(new ComplexCart(5,6));
        System.out.println(test);
    }
}