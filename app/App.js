import { StatusBar } from 'expo-status-bar';
// importing webview
import { WebView } from 'react-native-webview';

export default function App() {
  return (
    <WebView
      source={{ uri: 'https://www.itsreaddy.com/' }}
      style={{ marginTop: 20 }}
    />
    );
}

