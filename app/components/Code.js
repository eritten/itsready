import {View, Text, TextInput, TouchableOpacity} from 'react-native';
import React, {useState} from 'react';

export default function Code({navigation}) {
    const [code, setCode] = useState('');
    const [confirm, setConfirm] = useState(null);
    return (
        <View>
    <Text>Enter verification code</Text>
    <TextInput
        placeholder="Enter verification code"
        onChangeText={setCode}
        value={code}
    />
<TouchableOpacity>
    <Text>Confirm</Text>
    </TouchableOpacity>

    </View>
);
}