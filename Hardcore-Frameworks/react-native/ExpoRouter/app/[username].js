import  { Text, SafeAreaView, StyleSheet, Button} from 'react-native';
import { useRouter , useSearchParams} from 'expo-router';

const profile = () => {
    const router = useRouter();
    const {name, username} = useSearchParams();

    return (
        <SafeAreaView style={styles.container}>
            <Text style={styles.subtitle}>This is profile view for {name}(@{username}) </Text>
            <Button onPress={() => router.back()} title={"Go back!"}/>
        </SafeAreaView>
    )
}

export default profile;


const styles = StyleSheet.create({
    container: {
      flex: 1,
      alignItems: "center",
      padding: 24,
    },
    main: {
      flex: 1,
      justifyContent: "center",
      maxWidth: 960,
      marginHorizontal: "auto",
    },
    title: {
      fontSize: 64,
      fontWeight: "bold",
    },
    subtitle: {
      fontSize: 36,
      color: "#38434D",
    },
  });