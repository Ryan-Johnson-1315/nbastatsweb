<template>
  <v-container>
      <v-navigation-drawer
        app
        permanent
        expand-on-hover
        absolute
        disable-resize-watcher
        width="100"
      >
        <v-list
          nav
          dense
        >
          <v-list-item
            link
            to="/"
          >
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>
          <v-list-item
            link
            to="/about"
          >
            <v-list-item-icon>
              <v-icon>mdi-poll</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Stats</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
      <router-view/>
  </v-container>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue"
export default {
  components: [
    HelloWorld,
  ]
}
</script>

<style>

</style>
