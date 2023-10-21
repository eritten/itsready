import { View, Text, Button, SafeAreaView, TouchableOpacity } from 'react-native';
import React, { useState, useEffect } from 'react';
// import async storage
import AsyncStorage from '@react-native-async-storage/async-storage';
import Page from "./Page";
import Dashboard from "./Dashboard";

export default function Home({navigation}) {
const [auth, setAuth] = useState({})        
useEffect(() => {
AsyncStorage.getItem('auth')
.then(res => {
    if(res) {
        setAuth(JSON.parse(res))
    }
})
    
})

return (
    <>
{auth.isLogin ? <SafeAreaView> <Text>Home</Text> </SafeAreaView>: <SafeAreaView> <View>><Text>love page</Text></View> </SafeAreaView>}
   </>
)

}