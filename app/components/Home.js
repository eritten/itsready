import { View, Text, Button, SafeAreaView, TouchableOpacity } from 'react-native';

export default function Home({navigation}) {
    return (
<SafeAreaView>
    <Text>Itsreaddy Home</Text>
    <TouchableOpacity onPress={() => navigation.navigate('Signup')}>
        <Text>Signup</Text>
    </TouchableOpacity>
    <TouchableOpacity onPress={() => navigation.navigate('Login')}>
        <Text>Login</Text>
    </TouchableOpacity>
</SafeAreaView>
    )
}