<template>
  <v-container>
      <v-navigation-drawer
        app
        permanent
        expand-on-hover
        width="100"
      >
        <v-list
          nav
        >
          <v-list-item
            link
            to="/"
          >
            <v-list-item-icon>
              <v-icon>
                mdi-home
              </v-icon>
            </v-list-item-icon>
            <v-list-item>
              Home
            </v-list-item>
          </v-list-item>
          <v-list-item
            link
            to="/about"
          >
            <v-list-item-icon>
              <v-icon>
                mdi-poll
              </v-icon>
            </v-list-item-icon>
            <v-list-item>
              Stats
            </v-list-item>
          </v-list-item>
          <v-list-item
            link
            to="/career"
          >
            <v-list-item-icon>
              <v-icon
              >
                mdi-altimeter
              </v-icon>
            </v-list-item-icon>
            <v-list-item>
              Career
            </v-list-item>
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
