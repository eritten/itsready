import React, {useState}  from 'react';
import {SafeAreaView, Text, View, Button, TouchableOpacity} from 'react-native';

export default function Page({navigation}) {
return (
<View style={{flex: 1, alignItems: 'center', justifyContent: 'center'}}>
<Text>ITSREADY Home</Text>
<TouchableOpacity onPress={navigation.navigate("Signup")}>
    <Text>Signup</Text>
    </TouchableOpacity>
    <TouchableOpacity onPress={navigation.navigate("Login")}>
    <Text>Login</Text>
    </TouchableOpacity>
    </View>

)
}