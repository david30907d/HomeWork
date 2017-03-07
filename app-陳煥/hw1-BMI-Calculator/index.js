import React, { Component } from 'react';
import { AppRegistry, Text, TextInput, View } from 'react-native';

class PizzaTranslator extends Component {
  constructor(props) {
    super(props);
    this.state = {height: 0, weight:0};
  }

  render() {
    return (
      <View style={{padding: 10}}>
        <TextInput
          style={{height: 40}}
          placeholder="請輸入身高"
          onChangeText={(height) => this.setState({height})}
        />
        <TextInput
          style={{height: 40}}
          placeholder="請輸入體重"
          onChangeText={(weight) => this.setState({weight})}
        />
        <Text style={{padding: 10, fontSize: 42}}>
         
          BMI：{ parseFloat(this.state.weight)/Math.pow(parseFloat(this.state.height), 2)}
        </Text>
      </View>
    );
  }
}

AppRegistry.registerComponent('PizzaTranslator', () => PizzaTranslator);