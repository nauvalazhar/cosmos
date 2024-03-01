// This is an extended Java example designed to test overflow and syntax highlighting in your text editor.

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, extended Java example!");

        ArrayList<String> list = new ArrayList<>();
        list.add("Item 1");
        list.add("Item 2");

        for (String item : list) {
            System.out.println(item);
        }

        Map<String, Integer> map = new HashMap<>();
        map.put("key1", 100);
        map.put("key2", 200);

        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
        }

        new Thread(() -> {
            System.out.println("This is a thread running in Java.");
        }).start();
    }
}
