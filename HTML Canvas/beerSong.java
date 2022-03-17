//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by FernFlower decompiler)
//

package chap01;

public class BeerSong {
    public BeerSong() {
    }

    public static void main(String[] var0) {
        int var1 = 99;
        String var2 = "bottles";

        while(var1 > 0) {
            if (var1 == 1) {
                var2 = "bottle";
            }

            System.out.println(var1 + " " + var2 + " of beer on the wall");
            System.out.println(var1 + " " + var2 + " of beer");
            System.out.println("Take one down.");
            System.out.println("Pass it around.");
            --var1;
            if (var1 > 0) {
                System.out.println(var1 + " " + var2 + " of beer on the wall");
            } else {
                System.out.println("No more bottles of beer on the wall");
            }
        }

    }
}