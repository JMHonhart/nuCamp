//TODO: TASK ONE

// In the file workshop5.js, create a class with the name of Student. It will not inherit from any other class.
// Give the class a constructor with the parameters: name and email.
//     In the constructor, assign the name and email arguments to class properties of the same name, using
//     the this keyword. Review Exercise: JavaScript Classes if needed.
class Student {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }
}

testStudent = new Student('Bugs Bunny', 'bugs@bunny.com');
console.log(testStudent);
if (testStudent.name === 'Bugs Bunny' && testStudent.email === 'bugs@bunny.com') {
    console.log('TASK 1: PASS');
}


//TODO: Task TWO

// In the workshop5.js file, create another class named Bootcamp below the Student class.
// Give this class a constructor with the parameters of name, level, and a third parameter
// students which is initialized as an empty array (using default function parameters syntax).
// In the constructor, as in Task 1, assign the name, level, and students arguments to class
// properties of the same name, using the this keyword. Review Exercise: JavaScript Classes if needed.
// reactBootcamp = new Bootcamp("React", "Advanced");
// console.log(reactBootcamp);
// if ( reactBootcamp.name === 'React' && reactBootcamp.level === 'Advanced'
//     && Array.isArray(reactBootcamp.students) && reactBootcamp.students.length === 0) {
//     console.log('TASK 2: PASS');
// }

class Bootcamp {
    constructor(name, level, students) {
        this.name = name;
        this.level = level;
        this.students = [];
    }
}
reactBootcamp = new Bootcamp("React", "Advanced");
console.log(reactBootcamp);
if (reactBootcamp.name === 'React' && reactBootcamp.level === 'Advanced'
    && Array.isArray(reactBootcamp.students) && reactBootcamp.students.length === 0) {
    console.log('TASK 2: PASS');
}

//TODO: Task 3

//Add a method to the bootcamp class
//one parameter, student two register

const runTest = (bootcamp, student) => {
    const attemptOne = bootcamp.registerStudent(student);
    const attemptTwo = bootcamp.registerStudent(student);
    const attemptThree = bootcamp.registerStudent(new Student("Babs Bunny"));
    if (attemptOne && !attemptTwo && !attemptThree) {
        console.log("TASK 3: PASS");
    }

    //TODO: Task4
    //no parameters needed
    bootcamp.registerStudent(new Student('Babs Bunny', 'babs@bunny.com'));
    if (bootcamp.listStudents()) {
        console.log("TASK 4: PASS 1/2");
    }
    bootcamp.students = [];
    if (!bootcamp.listStudents()) {
        console.log("TASK 4: PASS 2/2");
    }



};

//calling or invoking the function
runTest(reactBootcamp, testStudent);
