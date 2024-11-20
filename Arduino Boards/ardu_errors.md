Aquí tienes un listado de errores comunes en Arduino junto con un mini ejemplo y el mensaje de error que podría arrojar el compilador:

### 1. **Error de tipo: Asignar un `char` a un `int`**
   **Ejemplo:**
   ```cpp
   int num = 'A'; // Caracter asignado a un int
   ```
   **Error:**
   ```
   warning: narrowing conversion of '65' from 'char' to 'int' inside { } [-Wnarrowing]
   ```

### 2. **Error de tipo: Asignar un `float` a un `int`**
   **Ejemplo:**
   ```cpp
   int num = 3.14; // Intentando asignar un float a un int
   ```
   **Error:**
   ```
   warning: narrowing conversion of '3.14' from 'float' to 'int' inside { } [-Wnarrowing]
   ```

### 3. **Error de tipo: Asignar un `String` a un `char[]`**
   **Ejemplo:**
   ```cpp
   char message[10] = "Hola";
   message = "Adiós"; // Intento de asignación directa
   ```
   **Error:**
   ```
   error: incompatible types in assignment of 'const char [6]' to 'char [10]'
   ```

### 4. **Falta de declaración de una variable**
   **Ejemplo:**
   ```cpp
   void setup() {
     int a = 5;
     b = 10; // 'b' no ha sido declarado
   }
   ```
   **Error:**
   ```
   error: 'b' was not declared in this scope
   ```

### 5. **Uso de una función no declarada**
   **Ejemplo:**
   ```cpp
   void setup() {
     int x = suma(5, 6); // La función 'suma' no ha sido declarada
   }
   ```
   **Error:**
   ```
   error: 'suma' was not declared in this scope
   ```

### 6. **Error de sintaxis: Llave de cierre faltante**
   **Ejemplo:**
   ```cpp
   void setup() {
     int a = 10;
     if (a > 5) {
       Serial.println("Mayor que 5");
   // Llave de cierre faltante
   ```
   **Error:**
   ```
   error: expected '}' at end of input
   ```

### 7. **Error por no usar paréntesis en una condición**
   **Ejemplo:**
   ```cpp
   void setup() {
     int a = 10;
     if a > 5 // Paréntesis faltantes
       Serial.println("Mayor que 5");
   }
   ```
   **Error:**
   ```
   error: expected primary-expression before '>' token
   ```

### 8. **Acceder a un índice fuera de los límites de un array**
   **Ejemplo:**
   ```cpp
   int numeros[5] = {1, 2, 3, 4, 5};
   int x = numeros[6]; // Índice fuera de los límites
   ```
   **Error:**
   ```
   warning: array subscript is above array bounds
   ```

### 9. **Asignación en lugar de comparación en un `if`**
   **Ejemplo:**
   ```cpp
   void setup() {
     int a = 5;
     if (a = 10) { // Asignación en vez de comparación
       Serial.println("a es 10");
     }
   }
   ```
   **Error:**
   ```
   warning: suggest parentheses around assignment used as truth value
   ```

### 10. **Uso de una función que no retorna un valor**
   **Ejemplo:**
   ```cpp
   int suma() {
     int x = 5 + 6;
   } // No retorna ningún valor
   ```
   **Error:**
   ```
   warning: control reaches end of non-void function
   ```

### 11. **Declarar variables fuera de los límites de una función**
   **Ejemplo:**
   ```cpp
   int a = 5;
   void setup() {
     int b = 10;
   }
   b = 15; // Intentando usar 'b' fuera de su scope
   ```
   **Error:**
   ```
   error: 'b' was not declared in this scope
   ```

### 12. **Uso de `return` en una función `void`**
   **Ejemplo:**
   ```cpp
   void suma() {
     return 5; // Intentando retornar un valor en una función void
   }
   ```
   **Error:**
   ```
   error: void function 'suma' should not return a value
   ```

### 13. **Operación entre tipos incompatibles**
   **Ejemplo:**
   ```cpp
   int a = 10;
   char b = 'A';
   int c = a + b; // Suma de un int y un char
   ```
   **Error:**
   ```
   warning: invalid conversion from 'int' to 'char'
   ```

Estos son algunos de los errores más comunes que puedes encontrar al programar en Arduino. Es importante estar atento a los tipos de datos y las declaraciones para evitar errores durante la compilación.

Aquí tienes algunos errores adicionales, incluyendo el error de falta de punto y coma, y otros que suelen ocurrir en Arduino:

### 14. **Falta de punto y coma (`;`)**
   **Ejemplo:**
   ```cpp
   void setup() {
     int a = 5 // Falta de punto y coma
   }
   ```
   **Error:**
   ```
   error: expected ';' before '}' token
   ```

### 15. **Variable fuera de alcance (scope)**
   **Ejemplo:**
   ```cpp
   void setup() {
     if (true) {
       int a = 5;
     }
     Serial.println(a); // 'a' fuera de alcance
   }
   ```
   **Error:**
   ```
   error: 'a' was not declared in this scope
   ```

### 16. **Llamar a una función antes de su declaración**
   **Ejemplo:**
   ```cpp
   void setup() {
     int x = suma(3, 4); // Intento de llamar a suma antes de su declaración
   }

   int suma(int a, int b) {
     return a + b;
   }
   ```
   **Error:**
   ```
   error: 'suma' was not declared in this scope
   ```

### 17. **Array con tamaño no constante**
   **Ejemplo:**
   ```cpp
   void setup() {
     int a = 5;
     int arr[a]; // No se puede usar una variable para definir el tamaño del array
   }
   ```
   **Error:**
   ```
   error: size of array 'arr' is not an integral constant-expression
   ```

### 18. **Uso incorrecto de `const`**
   **Ejemplo:**
   ```cpp
   void setup() {
     const int a = 10;
     a = 20; // Intentando cambiar una constante
   }
   ```
   **Error:**
   ```
   error: assignment of read-only variable 'a'
   ```

### 19. **Tipo de retorno de la función incorrecto**
   **Ejemplo:**
   ```cpp
   int suma() {
     return "Hola"; // Retornando un string en una función int
   }
   ```
   **Error:**
   ```
   error: invalid conversion from 'const char*' to 'int'
   ```

### 20. **División por cero**
   **Ejemplo:**
   ```cpp
   void setup() {
     int a = 10;
     int b = 0;
     int c = a / b; // División por cero
   }
   ```
   **Error:**
   ```
   warning: division by zero
   ```

### 21. **Operación con valores fuera del rango del tipo de dato**
   **Ejemplo:**
   ```cpp
   void setup() {
     byte a = 300; // Valor fuera del rango de 0-255 para tipo byte
   }
   ```
   **Error:**
   ```
   warning: large integer implicitly truncated to unsigned type
   ```

### 22. **Uso incorrecto de operadores**
   **Ejemplo:**
   ```cpp
   void setup() {
     int a = 5;
     int b = a ** 2; // Error en la operación de potencia
   }
   ```
   **Error:**
   ```
   error: invalid operands of types 'int' and 'int' to binary 'operator*'
   ```

### 23. **Incompatibilidad entre `void` y `return`**
   **Ejemplo:**
   ```cpp
   void setup() {
     return 0; // No se puede retornar un valor en una función 'void'
   }
   ```
   **Error:**
   ```
   error: void function 'setup' should not return a value
   ```

### 24. **Declaración de función sin cuerpo**
   **Ejemplo:**
   ```cpp
   void setup();
   ```
   **Error:**
   ```
   error: function definition does not declare parameters
   ```

### 25. **Uso de variables sin inicializar**
   **Ejemplo:**
   ```cpp
   void setup() {
     int a;
     Serial.println(a); // 'a' no ha sido inicializado
   }
   ```
   **Error:**
   ```
   warning: 'a' is used uninitialized in this function
   ```

Estos errores cubren una variedad de situaciones comunes al programar en Arduino, y al corregirlos, el compilador debería poder generar el código sin problemas. Estar atento a estos errores te permitirá depurar más rápido y evitar problemas durante la ejecución del programa.

Aquí tienes algunos errores comunes relacionados con el uso de **objetos** en Arduino, con ejemplos y los mensajes de error que podrías ver en el compilador:

### 26. **Acceso a un miembro no declarado en una clase**
   **Ejemplo:**
   ```cpp
   class MyClass {
   public:
     int x;
   };

   void setup() {
     MyClass obj;
     obj.y = 10; // Intentando acceder a un miembro no declarado
   }
   ```
   **Error:**
   ```
   error: 'class MyClass' has no member named 'y'
   ```

### 27. **Llamar a un método que no está definido**
   **Ejemplo:**
   ```cpp
   class MyClass {
   public:
     void myMethod();
   };

   void setup() {
     MyClass obj;
     obj.myMethod(); // Método declarado pero no definido
   }

   // Faltaría la implementación de 'myMethod'
   ```
   **Error:**
   ```
   error: undefined reference to 'MyClass::myMethod()'
   ```

### 28. **Uso de un constructor que no existe**
   **Ejemplo:**
   ```cpp
   class MyClass {
   public:
     MyClass(int a) {} // Constructor que acepta un parámetro
   };

   void setup() {
     MyClass obj; // No existe un constructor por defecto
   }
   ```
   **Error:**
   ```
   error: no matching function for call to 'MyClass::MyClass()'
   ```

### 29. **Llamada a un método `private` desde fuera de la clase**
   **Ejemplo:**
   ```cpp
   class MyClass {
   private:
     void myPrivateMethod() {}
   };

   void setup() {
     MyClass obj;
     obj.myPrivateMethod(); // Intento de acceder a un método privado
   }
   ```
   **Error:**
   ```
   error: 'void MyClass::myPrivateMethod()' is private within this context
   ```

### 30. **Uso de punteros a objetos sin inicializar**
   **Ejemplo:**
   ```cpp
   class MyClass {
   public:
     int x;
   };

   void setup() {
     MyClass *obj; // Puntero no inicializado
     obj->x = 10;  // Intento de acceso a través de puntero no inicializado
   }
   ```
   **Error:**
   ```
   error: invalid use of member (did you forget to dereference the pointer?)
   ```

### 31. **Olvidar el operador `new` al usar punteros a objetos**
   **Ejemplo:**
   ```cpp
   class MyClass {
   public:
     int x;
   };

   void setup() {
     MyClass *obj; // Puntero declarado pero no asignado con new
     obj->x = 10;  // Intento de usar puntero sin asignar
   }
   ```
   **Error:**
   ```
   error: invalid use of member (did you forget to dereference the pointer?)
   ```

### 32. **Redefinición de un método virtual sin especificar `override`**
   **Ejemplo:**
   ```cpp
   class Base {
   public:
     virtual void myMethod() {}
   };

   class Derived : public Base {
   public:
     void myMethod() {} // Se espera un 'override'
   };

   void setup() {
     Derived obj;
     obj.myMethod();
   }
   ```
   **Error:**
   ```
   warning: 'void Derived::myMethod()' hides inherited virtual function
   ```

### 33. **Crear un objeto de una clase abstracta**
   **Ejemplo:**
   ```cpp
   class AbstractClass {
   public:
     virtual void myMethod() = 0; // Método puramente virtual
   };

   void setup() {
     AbstractClass obj; // No se puede instanciar una clase abstracta
   }
   ```
   **Error:**
   ```
   error: cannot declare variable 'obj' to be of abstract type 'AbstractClass'
   ```

### 34. **Acceso a miembros estáticos sin usar el nombre de la clase**
   **Ejemplo:**
   ```cpp
   class MyClass {
   public:
     static int x;
   };

   void setup() {
     MyClass obj;
     obj.x = 10; // Intento de acceder a un miembro estático mediante el objeto
   }
   ```
   **Error:**
   ```
   error: cannot access static member 'MyClass::x' in non-static context
   ```

### 35. **Problema con el uso de destructores en objetos dinámicos**
   **Ejemplo:**
   ```cpp
   class MyClass {
   public:
     ~MyClass() {
       Serial.println("Destructor llamado");
     }
   };

   void setup() {
     MyClass *obj = new MyClass();
     // Falta delete obj; // No se libera la memoria, hay fuga de memoria
   }
   ```
   **Error:**
   ```
   (No hay un error específico de compilador, pero podría causar problemas de memoria)
   ```

### 36. **Olvidar inicializar un miembro de una clase con el constructor**
   **Ejemplo:**
   ```cpp
   class MyClass {
   public:
     int x;
     MyClass() {} // No inicializa 'x'
   };

   void setup() {
     MyClass obj;
     Serial.println(obj.x); // 'x' no ha sido inicializado
   }
   ```
   **Error:**
   ```
   warning: 'x' is used uninitialized in this function
   ```

Estos son errores comunes relacionados con el manejo de **objetos y clases** en Arduino. Muchos de ellos se deben a la incorrecta declaración, uso o manejo de los métodos y constructores en las clases, algo habitual cuando se comienza a trabajar con programación orientada a objetos en C++.
