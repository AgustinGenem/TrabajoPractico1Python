package Python.Practico_1;

import java.util.Random;
import java.util.Scanner;

public class Ejercicio14 {
    public static void main(String[] args) {
        Random random = new Random();
        Scanner sc = new Scanner(System.in);
        int num = random.nextInt(0,101);
        int intentos = 0;

        while (true) {
            intentos ++;
            System.out.println("Ingrese un numero");
            int respuesta = sc.nextInt();
            if (respuesta > num) {
                System.out.println("Numero muy alto");
            }
    
            if (respuesta < num) {
                System.out.println("Numero muy bajo");
            }

            if (respuesta == num) {
                System.out.println("!!Numero Correcto!!");
                System.out.println("Cantidad de intentos: " + intentos);
                break;
            }

        }
       sc.close();
    }
    
}
