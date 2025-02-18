//Rechner.cpp

#include <iostream>

int addition(int a, int b){
    return a+b;
}

int subtraktion(int a, int b){
    return a-b;
}

int multiplikation(int a, int b){
    return a*b;
}

int division(int a, int b){
    return a/b;
}

int main(){
    printf("Willkomen\n")
    std::cout << "Willkommen\n";
    int a, b;
    std::cout << "Bitte geben Sie die erste Zahl ein: ";
    std::cin >> a;
    std::cout << "Bitte geben Sie die zweite Zahl ein: ";
    std::cin >> b;
    
    std::cout << "Bitte wählen Sie den gewünschten Rechenoperator aus: \n";
    char op;
    std::cin >> op;

    if(op == '+'){
        std::cout << "Das Ergebnis ist: " << addition(a, b) << std::endl;
    } else if(op == '-'){
        std::cout << "Das Ergebnis ist: " << subtraktion(a, b) << std::endl;
    } else if(op == '*'){
        std::cout << "Das Ergebnis ist: " << multiplikation(a, b) << std::endl;
    } else if(op == '/'){
        do {
            if(b != 0){
                std::cout << "Das Ergebnis ist: " << division(a, b) << std::endl;
                break;
            } else {
                std::cout << "Sie können nicht durch 0 teilen, bitte geben Sie eine andere Zahl ein: ";
                std::cin >> b;
            }
        } while(true);
    }

    std::cout << "Vielen Dank, auf Wiedersehen!" << std::endl;
    return 0;
}