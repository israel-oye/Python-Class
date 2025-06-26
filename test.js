let studentDetails = {
    school: 'AU College',
    location: 'Osun',
    isElite: true
};

studentDetails.school;

// Serialization in Javascript
console.log(JSON.stringify(studentDetails));


// fetch('/user.json')
//     .then(res => {
//         res.json()
//     })
//     .then(data => {
//         console.log(data)
//     });