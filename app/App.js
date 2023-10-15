import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import Home from './components/Home';
import Signup from './components/Signup';
import Login from './components/Login';
import Reset from './components/Reset';
import Code from './components/Code';

const Stack = createStackNavigator();

export default function App() {
    return (
<NavigationContainer>
<Stack.Navigator initialRouteName="Home">
<Stack.Screen name="Home" component={Home} />
<Stack.Screen name="Signup" component={Signup} />
<Stack.Screen name="Login" component={Login} />
<Stack.Screen name="Reset" component={Reset} />
<Stack.Screen name="Code" component={Code} />
</Stack.Navigator>
</NavigationContainer>
    )
}