<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl">Sign up</h1>

                <p class="mb-6 text-gray-500">
                    Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate.
                    Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate.
                </p>

                <p class="font-bold">
                    Already have an account? <RouterLink :to="{'name': 'login'}" class="underline">Click here</RouterLink> to log in!
                </p>
            </div>
        </div>

        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <!-- on submit, prevent default, and call the submitForm methods -->
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label>Name</label><br>
                        <input type="text" v-model="form.name" placeholder="Your full name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>E-mail</label><br>
                        <input type="email" v-model="form.email" placeholder="Your e-mail address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Password</label><br>
                        <input type="password" v-model="form.password1" placeholder="Your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Repeat password</label><br>
                        <input type="password" v-model="form.password2" placeholder="Repeat your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6" role="alert">
                            <ul>
                                <li v-for="error in errors" :key="error">{{ error }}</li>
                            </ul>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Sign up</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import { useToastStore } from '../stores/toast'

    export default{
        setup() {
            const toastStore = useToastStore()

            return {
                toastStore
            }
        },

        data() {
            return {
                form: {
                    email: '',
                    name: '',
                    password1: '',
                    password2: ''
                },
                errors: [],
            }
        },
        methods: {
            submitForm() {
                this.errors = []

                if (this.form.name==='') {
                    this.errors.push('Name required.')
                }
                if (this.form.email==='') {
                    this.errors.push('Email required.')
                }
                if (this.form.password1==='') {
                    this.errors.push('Password required.')
                }
                if (this.form.password2==='') {
                    this.errors.push('Password confirmation required.')
                }
                if (this.form.password1 !== this.form.password2) {
                    this.errors.push('Passwords do not match.')
                }

                if (this.errors.length === 0) {
                    axios.post('/api/signup/', this.form)
                        .then(response => {
                            this.toastStore.showToast(5000, 'user is registered, please login,', 'success')

                            // reset the form
                            this.form.name = ''
                            this.form.email = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                        })
                        .catch(error => {
                            this.toastStore.showToast(5000, error.response.data.message, 'danger')
                            this.errors.push(error.message)
                        })
                }
            }
        }
    }

</script>