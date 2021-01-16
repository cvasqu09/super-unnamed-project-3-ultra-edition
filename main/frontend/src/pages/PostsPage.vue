<template>
  <div>
    <header>
      <h1>Posts</h1>
    </header>
    <section>
      <post-card v-for="post in posts" :key="post.id"
                 :title="post.title"
                 :description="post.description"
                 :date="post.createdAt"
      ></post-card>
    </section>
  </div>
</template>

<script>
import PostCard from '@/components/posts/PostCard.vue';
import axios from 'axios';
import { DateTime } from 'luxon';

export default {
  name: 'PostsPage',
  components: { PostCard },
  data() {
    return {
      posts: [],
    };
  },
  mounted() {
    axios.get('/posts/').then((res) => {
      const retrievedPosts = res.data;
      this.posts = retrievedPosts.map((post) => ({
        title: post.title,
        description: post.description,
        createdAt: DateTime.fromISO(post.createdAt).toLocaleString(DateTime.DATE_MED),
      }));
    });
  },
};
</script>

<style scoped>

</style>
