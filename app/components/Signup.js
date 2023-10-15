import{ React, useState } from 'react';
import { TextInput, Text,View, Button, StyleSheet, TouchableOpacity } from 'react-native';
// importing axios 
import axios from 'axios';

export default function Signup({ navigation }) {
    const [hidden, setHidden] = useState(true);
    const [text, setText] = useState('Show Password');
const [username, setUsername] = useState('');
const [email, setEmail] = useState('');
const [password, setPassword] = useState('');
const [confirmPassword, setConfirmPassword] = useState('');
function  Signup() {
    axios.post('http://localhost:8000/api/create_account/', {
        username: username,
        email: email,
        password: password
    })
    .then(function (response) {
        alert(response);
    })
    .catch(function (error) {
       alert(error);
    });

}
    function showPassword() {
if (hidden){ 
    setHidden(false);
setText('Hide Password');
}
else {
    setHidden(true);
    setText('Show Password');
}}



return (
    <View>
<Text>Use below form to signup</Text>
<TextInput placeholder="Username" onChangeText={setUsername} />
<TextInput placeholder="Email" keyboardType="email-address" onChangeText={setEmail} />
<TextInput placeholder="Password" secureTextEntry={hidden} onChangeText={setPassword} />
<TouchableOpacity onPress={showPassword}>
<Text>{text}</Text>
</TouchableOpacity>

<TextInput placeholder="Confirm Password" secureTextEntry={hidden} />
<TouchableOpacity onPress={showPassword}>
<Text>{text}</Text>
</TouchableOpacity>
<Button title="Signup" onPress={Signup} />

<TouchableOpacity onPress={() => navigation.navigate('Login')}>
<Text>Already have an account? Login</Text>
</TouchableOpacity>
</View>
)
}