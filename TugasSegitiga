#include <stdio.h>

int main() {
    float a, b, c, temp;

    printf("Masukkan tiga sisi segitiga (a b c): ");
    scanf("%f %f %f", &a, &b, &c);

    // Jika ada sisi <= 0
    if (a <= 0 || b <= 0 || c <= 0) {
        printf("Tidak dapat membentuk segitiga.\n");
        return 0;
    }

    // Urutkan supaya a <= b <= c
    if (a > b) { temp = a; a = b; b = temp; }
    if (b > c) { temp = b; b = c; c = temp; }
    if (a > b) { temp = a; a = b; b = temp; }

    // Jika tidak memenuhi syarat segitiga
    if (c >= a + b) {
        printf("Tidak dapat membentuk segitiga.\n");
        return 0;
    }

    // Cek jenis segitiga
    if (a == b && b == c)
        printf("Segitiga Sama Sisi (Equilateral)\n");
    else if (a == b || b == c || a == c)
        printf("Segitiga Sama Kaki (Isosceles)\n");
    else if (c * c == a * a + b * b)
        printf("Segitiga Siku-Siku (Right Triangle)\n");
    else
        printf("Segitiga Bebas (Scalene)\n");

    return 0;
}
