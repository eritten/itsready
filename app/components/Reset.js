import {View, Text, Button, StyleSheet, TouchableOpacity, TextInput} from 'react-native';
import React, { useState } from 'react';

export default function Reset({navigation}) {

    return (
        <View>
            <Text>Reset Password</Text>
            <TextInput placeholder="Email" keyboardType="email-address" />
            <Button title="Reset" onPress={() => navigation.navigate('Login')} />
            <TouchableOpacity onPress={() => navigation.navigate('Login')}>
                <Text>Back to Login</Text>
            </TouchableOpacity>
        </View>
    )
}