import {Text, TextInput, View, Button, TouchableOpacity, StyleSheet} from 'react-native';
import React, { useState } from 'react';
import axios from 'axios';
// import sync storage
import AsyncStorage from '@react-native-async-storage/async-storage';

export default function Login({navigation}) {
const [user, setUser] = useState('');
const [password, setPassword] = useState('');
const [error, setError] = useState('');
const [loading, setLoading] = useState(false);
    const [hidden, setHidden] = useState(true);
    const [text, setText] = useState('Show Password');
    function showPassword() {
if (hidden){ 
    setHidden(false);
setText('Hide Password');
}
else {
    setHidden(true);
    setText('Show Password');
}
}


function login() {
axios.post("https://www.itsreaddy.com/api/login/", {"username": user, "password": password})
.then((res) => {
const data = {"username": res.data.username, "email": res.data.email, "id": res.data.user_id, "isLogin": true}

AsyncStorage.setItem("auth", JSON.stringify(data))
navigation.navigate("Home")

})
.catch((err) => alert(err))
}

return (
    <View>
<Text>Login</Text>
<TextInput placeholder="Username Or Email" onChangeText={setUser} />
<TextInput placeholder="Password" secureTextEntry={hidden} onChangeText={setPassword} />
<TouchableOpacity onPress={showPassword}>
<Text>{text}</Text>

</TouchableOpacity>
<Button title="Login" onPress={login} />
<Button title="Signup" onPress={() => navigation.navigate('Signup')} />
<Button title="Reset Password" onPress={() => navigation.navigate('Reset')} />
</View>
)
}