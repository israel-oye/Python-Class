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
let data = `{
 "1": 101,
 "name": "Segun",
 "job": "Professional Doom Scroller",
 "is_employed": false,
 "friends": [
  "Shaul",
  "Yitzchak",
  "Shimeon",
  "Yochanan"
 ]
}`
let newObj = JSON.parse(data);

console.log(newObj.friends.length);