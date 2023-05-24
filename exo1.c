int main() {
    int age = 80;
    float poids = 80;
    char initial = 'A';
    long distance = 150000;
    double pi = 3.14159;
    short nombre = 100;
    unsigned int compte = 1000;
    char nom[20] = "Davy Jones";
    unsigned long long population = 7896541230;
    unsigned short code = 12345;
    
    printf("Age: %d\n", age);
    printf("Poids: %.2f\n", poids);
    printf("Initial: %c\n", initial);
    printf("Distance: %ld\n", distance);
    printf("Pi: %lf\n", pi);
    printf("Nombre: %hd\n", nombre);
    printf("Compte: %u\n", compte);
    printf("Nom: %s\n", nom);
    printf("Population: %llu\n", population);
    printf("Code: %hu\n", code);
    
    return 0;
}