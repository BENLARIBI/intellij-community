import java.util.List;

class Foo {
    <T> void method1(final T[] val) {
        class Inner {
            void method2() {
                for (T t : <selection>val</selection><caret>) {

                }
            }
        }
    }
}