var environments = {
  staging: {
    FIREBASE_API_KEY: "AIzaSyBqV7cOZWNmxiNAOOuOpI5oaYEzDaM_HLs",
    FIREBASE_AUTH_DOMAIN: "fine-blueprint-233308.firebaseapp.com",
    FIREBASE_DATABASE_URL: "https://fine-blueprint-233308.firebaseio.com",
    FIREBASE_PROJECT_ID: "fine-blueprint-233308",
    FIREBASE_STORAGE_BUCKET: "fine-blueprint-233308.appspot.com",
    FIREBASE_MESSAGING_SENDER_ID: "800073053224",
    GOOGLE_CLOUD_VISION_API_KEY: "AIzaSyALZ_DngRxh__h1Wp_xXSig4K21ZBdPxtY"
  },
  production: {
    // Warning: This file still gets included in your native binary and is not a secure way to store secrets if you build for the app stores. Details: https://github.com/expo/expo/issues/83
  }
};
function getReleaseChannel() {
  let releaseChannel = Expo.Constants.manifest.releaseChannel;
  if (releaseChannel === undefined) {
    return "staging";
  } else if (releaseChannel === "staging") {
    return "staging";
  } else {
    return "staging";
  }
}
function getEnvironment(env) {
  console.log("Release Channel: ", getReleaseChannel());
  return environments[env];
}
var Environment = getEnvironment(getReleaseChannel());
export default Environment;