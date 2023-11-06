public class Main {
    public static void main(String[] args) {
        Complex c_3minus4i = new ComplexCart(3, 4);
        Complex c_minus5plus6i = new ComplexCart(5,6);
        System.out.println(c_3minus4i);
        System.out.println(c_minus5plus6i);
        c_3minus4i.divide(c_minus5plus6i);
        System.out.println(c_3minus4i);
    }
}