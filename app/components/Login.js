import {Text, TextInput, View, Button, TouchableOpacity, StyleSheet} from 'react-native';
import React, { useState } from 'react';

export default function Login({navigation}) {
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
}}


return (
    <View>
<Text>Login</Text>
<TextInput placeholder="Username Or Email" />
<TextInput placeholder="Password" secureTextEntry={hidden} />
<TouchableOpacity onPress={showPassword}>
<Text>{text}</Text>

</TouchableOpacity>
<Button title="Login" onPress={() => navigation.navigate('Home')} />
<Button title="Signup" onPress={() => navigation.navigate('Signup')} />
<Button title="Reset Password" onPress={() => navigation.navigate('Reset')} />
</View>
)
}