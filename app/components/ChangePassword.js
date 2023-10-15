import {View, Text, TextInput, TouchableOpacity, Alert} from 'react-native';
import React, {useState} from 'react';

export default function ChangePassword({navigation}) {

    return (
        <View style={styles.container}>
            <Text>Change Password</Text>
<TextInput placeholder="Old Password" secureTextEntry={true} style={styles.input} />
<TextInput placeholder="New Password" secureTextEntry={true} style={styles.input} />
<TextInput placeholder="Confirm Password" secureTextEntry={true} style={styles.input} />
<TouchableOpacity style={styles.button} onPress={() => Alert.alert('Password Changed Successfully')}>
    <Text style={styles.buttonText}>Change Password</Text>
</TouchableOpacity>
        </View>
    );
}

const styles = StyleSheet.create({

    container: {
        flex: 1,
        backgroundColor: '#fff',
        justifyContent: 'center',
        padding: 20,
    },
    input: {
        height: 40,
        backgroundColor: '#ccc',
        marginBottom: 10,
        padding: 10,
        borderRadius: 5,
    },
    button: {
        backgroundColor: 'blue',
        padding: 10,
        borderRadius: 5,
    },
    buttonText: {
        fontSize: 20,
        color: '#fff',
        textAlign: 'center',
    },
});

